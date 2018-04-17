import sys
import functools
import operator
from base import kmers, most_probable_kmer

if __name__ == '__main__' :
    #
    # with open('downloads/profile_most_probable.txt','r') as f:
    #     text = f.readline().strip()
    #     k = int(f.readline().strip())
    #
    #     profile = [[] for x in 'ACGT']
    #     for nucleotide in xrange(4):
    #         words = f.readline().strip().split()
    #         profile[nucleotide] = [float(num) for num in words]
    #
    #     assert most_probable_kmer(k,text,profile) == 'CCGAG'

    with open('downloads/dataset_159_3.txt','r') as f :

        text = f.readline().strip()
        k = int(f.readline().strip())

        profile = [[] for x in 'ACGT']
        for nucleotide in xrange(4):
            words = f.readline().strip().split()
            profile[nucleotide] = [float(num) for num in words]

        print most_probable_kmer(k,text,profile)
