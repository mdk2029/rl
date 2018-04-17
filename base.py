from collections import Counter
import functools
import operator
import random

def kmers(dna, k) :
    dnalen = len(dna)
    for i in xrange(0,dnalen-k+1):
        yield dna[i:i+k]


def complement(N) :

    def complementary_nucleotide(N) :
        if N == 'A' :
            return 'T'
        if N == 'T' :
            return 'A'
        if N == 'C' :
            return 'G'
        if N == 'G' :
            return 'C'

        raise RuntimeError('Invalid argument : %c' % N)


    s = str()
    for c in N :
        s+=complementary_nucleotide(c)
    return s[::-1]


def hamming_distance(str1,str2) :

    assert len(str1) == len(str2)

    distance = 0
    for idx in xrange(0,len(str1)):
        if str1[idx] != str2[idx] :
             distance += 1

    return distance


def hamming_neighborhood(pattern,distance):

    def toggled(nucleotide) :
        if nucleotide == 'A' :
            return ['C','G','T']
        elif nucleotide == 'C' :
            return ['A','G','T']
        elif nucleotide == 'G' :
            return ['A','C','T']
        elif nucleotide == 'T':
            return ['A','C','G']
        else :
            raise RuntimeError('unknown nucleotide')

    def next_neighbors(pattern) :
        hood = set()
        plen = len(pattern)
        for j in xrange(0,plen):
            hood |= set( pattern[0:j] + str(n) + pattern[j+1:plen] for n in toggled(pattern[j]) )
        return hood

    neighbors = []
    for idx in xrange(0,distance+1):
        neighbors.append(set())

    neighbors[0].add(pattern)
    for idx in xrange(1,distance+1):
        for p in neighbors[idx-1]:
            neighbors[idx].update(next_neighbors(p))

    all_neighbors = set()
    for idx in xrange(0,distance+1):
        all_neighbors.update(neighbors[idx])

    return all_neighbors


def score(motifs) :
    """ Given a collection of motifs, assign a score to it.
        Identify the most frequent nuceleotide at an index
        Ignore it and count the others to get a number
        for that index. Sum across all indices
        AAAC
        CCAT
        CAGG
        TTGG
        2222 : 8
    """

    lengths = [len(m) for m in motifs]
    assert all([l == lengths[0] for l in lengths])
    rows = len(motifs)
    motiflen = lengths[0]

    score = 0
    for idx in xrange(motiflen):
        col = ''
        for r in xrange(rows):
            col += motifs[r][idx]
        most_freq = Counter(col).most_common(1)[0][1]
        score += (rows - most_freq)

    return score


def profile(motifs, pseudocounts=True) :
    """
    profile of a motif is a 4xk matrix with the probability distribution over each col.
    AA
    CC
    CA
    TT
    CG

    1/5 2/5
    3/5 1/5
    0/5 1/5
    1/5 1/5

    """

    lengths = [len(m) for m in motifs]
    assert all([l == lengths[0] for l in lengths])
    k = lengths[0]

    profile = [[0.0]*k for x in xrange(4)]
    for idx in xrange(k) :
        col = ''
        for m in motifs :
            col += m[idx]
        counts = dict(Counter(col))
        total = float(len(motifs))
        if pseudocounts:
            for n in 'ACGT':
                counts[n] = counts.get(n,0) + 1
            total += 4.0

        profile[0][idx] = counts.get('A',0)/total
        profile[1][idx] = counts.get('C',0)/total
        profile[2][idx] = counts.get('G',0)/total
        profile[3][idx] = counts.get('T',0)/total

    return profile


def most_probable_kmer(k,text,profile) :
    def nuc_idx(n):
        return "ACGT".find(n.upper())

    bestcandidate = text[0:k]
    bestprob = 0.0

    for candidate in kmers(text,k):
        prob = functools.reduce(operator.mul, [profile[nuc_idx(nuc)][idx] for idx,nuc in enumerate(candidate)], 1.0)
        if prob > bestprob :
            bestprob = prob
            bestcandidate = candidate

    return bestcandidate


class loaded_n_die :

    def __init__(self,distribution) :
        self.A = []
        self.A.append(distribution[0])
        for i in xrange(1,len(distribution)):
            self.A.append(self.A[i-1] + distribution[i])

    def roll(self):
        r = random.random()
        al = len(self.A)
        for i in xrange(al):
            if (self.A[i] > r) or (i == al):
                return i


def numberToPattern(number, length, rna=False) :
    switcher = {
        0 : 'A',
        1 : 'C',
        2 : 'G',
        3 : 'T' if not rna else 'U'
    }

    pattern = ''
    remaining = number
    for idx in xrange(length-1,-1,-1):
        num = remaining / pow(4,idx)
        remaining = remaining % pow(4,idx)
        pattern += switcher[num]

    return pattern


def patternToNumber(pattern) :
    """Convert a pattern from an alphabet from genome alphabet to a number"""

    switcher =  {
        'A' : 0,
        'a' : 0,
        'c' : 1,
        'C' : 1,
        'g' : 2,
        'G' : 2,
        'T' : 3,
        't' : 3,
        'U' : 3,
        'u' : 3
    }

    if(len(pattern)) == 1 :
        return switcher[pattern]

    else:
        return 4*patternToNumber(pattern[:-1]) + patternToNumber(pattern[-1])


def dna_to_rna(genome) :
    rna = str()
    for n in genome :
        rna += 'U' if n.upper() == 'T' else n.upper()
    return rna

def rna_to_dna(genome) :
    dna = str()
    for n in genome :
        dna += 'T' if n.upper() == 'U' else n.upper()
    return dna

