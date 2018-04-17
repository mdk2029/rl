from base import loaded_n_die, score, kmers, profile
import random
import functools
import operator

def gibbs_sampling_motif_search(dnastrs, k, t, N) :

    def generateInitialMotifs(dnastrs,k):
        maxidx = len(dnastrs[0]) - k
        assert(maxidx >= 0)

        initialMotifs = []
        for d in dnastrs :
            start = random.randint(0,maxidx)
            initialMotifs.append(d[start:start+k])

        return initialMotifs

    def profile_randomly_generated_kmer(text, k, prof):

        def nuc_idx(n):
            r = "ACGT".find(n.upper())
            return r

        probs = []
        for candidate in kmers(text,k):
            prob = functools.reduce(operator.mul, [prof[nuc_idx(nuc)][idx] for idx,nuc in enumerate(candidate)], 1.0)
            probs.append(prob)

        sum = functools.reduce(operator.add, probs, 0.0)
        probdist = [float(p)/float(sum) for p in probs]
        idx = loaded_n_die(probdist).roll()
        return text[idx:idx+k]


    assert(len(dnastrs) == t)
    initialMotifs = generateInitialMotifs(dnastrs,k)
    best = list(initialMotifs)
    bestscore = score(best)

    for j in xrange(N) :
        i = random.randint(0,t-1)
        reducedMotif = list(initialMotifs)
        del reducedMotif[i]
        pro = profile(reducedMotif,pseudocounts=True)
        motif_i = profile_randomly_generated_kmer(dnastrs[i],k,pro)
        reducedMotif = list(initialMotifs)
        reducedMotif[i] = motif_i
        reducedMotifScore = score(reducedMotif)
        if reducedMotifScore < bestscore :
            best = reducedMotif
            bestscore = reducedMotifScore

    return best


if __name__ == '__main__' :

    # k = 8
    # t = 5
    # N = 100
    #
    # dnastrs = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    #
    # best = gibbs_sampling_motif_search(dnastrs,k,t,N)
    # for b in best :
    #     print b


     with open('downloads/gibbs.txt','r') as f:

        f.readline()
        line = f.readline().strip().split()
        k = int(line[0])
        t = int(line[1])
        N = int(line[2])
        dnastrs = []
        for i in xrange(t):
            dnastrs.append(f.readline().strip())

        best = gibbs_sampling_motif_search(dnastrs,k,t,N)

        for b in best:
            print b
