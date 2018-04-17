import sys
from freqArray import patternToNumber, numberToPattern
from base import complement,hamming_neighborhood


def freqarray_with_mismatches_reverse(genome,k,distance):
    all_kmers_freq = [0]*(pow(4,k))
    max_freq = 0
    for idx in xrange(0,len(genome)-k+1):
        for current in [genome[idx:idx+k], complement(genome[idx:idx+k])] :
            dneighbors = hamming_neighborhood(current,distance)
            for neigh in dneighbors :
                rank = patternToNumber(neigh)
                all_kmers_freq[rank] = all_kmers_freq[rank]+1
                max_freq = max(max_freq,all_kmers_freq[rank])


    return (all_kmers_freq,max_freq)

def freq_with_mismatches_reverse(genome, k, distance) :
    all_kmers_freq,max_freq = freqarray_with_mismatches_reverse(genome,k,distance)
    most_freq = []
    for rank,freq in enumerate(all_kmers_freq):
        if freq == max_freq :
            most_freq.append(rank)

    ret = [numberToPattern(rank,k) for rank in most_freq]
    return ret


#def freq_with_mismatches_reverse(genome,k,distance) :

if __name__ == '__main__' :
    # print hamming_neighborhood("AT", 1)
    # print hamming_neighborhood("AT", 2)

    # genome = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    # k = 4
    # d = 1
    # ret = freq_with_mismatches_reverse(genome,k,d)
    # map(lambda x : sys.stdout.write("%s " % x), ret)

    #
    # with open("Downloads/dataset_9_8.txt") as f:
    #
    #     genome = f.readline().strip()
    #     kd = f.readline().strip().split()
    #     k = int(kd[0])
    #     d = int(kd[1])
    #
    #     ret = freq_with_mismatches_reverse(genome,k,d)
    #     map(lambda x : sys.stdout.write("%s " % x), ret)

    a = hamming_neighborhood('TGCAT', 2)
    print len(a)
    # map(lambda x : sys.stdout.write("%s " % x), a)