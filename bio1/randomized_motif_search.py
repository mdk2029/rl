from base import score,kmers,profile,most_probable_kmer
import sys
from random import randint, SystemRandom


def randomized_motif_search(dnastrs, k, t) :

    def generateInitialMotifs(dnastrs,k):
        maxidx = len(dnastrs[0]) - k
        assert(maxidx >= 0)

        initialMotifs = []
        for d in dnastrs :
            start = randint(0,maxidx)
            initialMotifs.append(d[start:start+k])

        return initialMotifs


    def best_motifs(dnastrs,initial_motifs,k) :

        def next_motifs(current_motifs, k) :
            pro = profile(current_motifs,pseudocounts=True)
            nxt = []
            for dna in dnastrs:
                nxt.append(most_probable_kmer(k,dna,pro))
            return nxt

        best = initial_motifs
        bestscore = score(initial_motifs)

        while True:
            n = next_motifs(best,k)
            ns = score(n)
            if ns < bestscore :
                best = n
                bestscore = ns
            else :
                return best


    best = None
    bestscore = sys.maxint

    for i in xrange(1000) :
        if i %100 == 0 :
            print("i = %d" % i)
        candidate = best_motifs(dnastrs,generateInitialMotifs(dnastrs,k),k)
        cscore = score(candidate)
        if cscore < bestscore :
            bestscore = cscore
            best = candidate

    return best


if __name__ == '__main__' :

    # k = 8
    # t = 5
    #
    # dnastrs = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
    #            'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    #
    # best = randomized_motif_search(dnastrs,k,t)
    # assert best == ['TCTCGGGG','CCAAGGTG','TACAGGCG','TTCAGGTG', 'TCCACGTG']


    dnastrs = ['ATGAGGTC','GCCCTAGA','AAATAGAT','TTGTGCTA']
    current_motifs = ['GTC','CCC', 'ATA', 'GCT']

    def next_motifs_1(current_motifs, k) :
            pro = profile(current_motifs,pseudocounts=True)
            nxt = []
            for dna in dnastrs:
                nxt.append(most_probable_kmer(k,dna,pro))
            return nxt

    n = next_motifs_1(current_motifs,3)
    for n1 in n :
        print n1


    # with open('downloads/dataset_161_5.txt','r') as f:
    #
    #     line = f.readline().strip().split()
    #     k = int(line[0])
    #     t = int(line[1])
    #     dnastrs = []
    #     for i in xrange(t):
    #         dnastrs.append(f.readline().strip())
    #
    #     best = randomized_motif_search(dnastrs,k,t)
    #
    #     for b in best:
    #         print b



