from base import score,kmers,profile
from profile_most_probable import most_probable_kmer
import sys

def greedy_motif(dnastrs, k, t, pseudocounts=True) :

    assert(len(dnastrs) >= t)

    best_motifs = [dna[0:k] for dna in dnastrs]
    best_score = score(best_motifs)

    for m in kmers(dnastrs[0],k):
        motifs = [m]
        for i in xrange(1,t) :
            current_profile = profile(motifs,pseudocounts=pseudocounts)
            new_motif = most_probable_kmer(k,dnastrs[i],current_profile)
            motifs.append(new_motif)

        s = score(motifs)
        if s < best_score :
            best_score = s
            best_motifs = motifs

    return best_motifs


if __name__ == '__main__' :


        # with open('downloads/dataset_159_5.txt','r') as f:
        #
        #     line = f.readline().strip()
        #     k = int(line.split()[0])
        #     t = int(line.split()[1])
        #     dnastrs = []
        #     for i in xrange(t) :
        #         dnastrs.append(f.readline().strip())
        #
        #     #dnastrs = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']
        #     a = greedy_motif(dnastrs,k,t)
        #     for s in a:
        #         print s
        # # assert score(motifs) == 8
        # #print profile(motifs)

        #
        # dnastrs = ['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']
        # a = greedy_motif(dnastrs, 3,5)
        # map(lambda s : sys.stdout.write('%s '% s), a)


    with open('downloads/dataset_160_9.txt','r') as f:

        line = f.readline().strip().split()
        k = int(line[0])
        t = int(line[1])
        dnastrs = []
        for i in xrange(t):
            dnastrs.append(f.readline().strip())

        a = greedy_motif(dnastrs,k,t)
        map(lambda s : sys.stdout.write('%s\n'% s), a)
