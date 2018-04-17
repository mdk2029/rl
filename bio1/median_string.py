import sys
import itertools
from base import kmers, hamming_distance

def min_distance1(kmer,dna) :
    return min([hamming_distance(kmer,candidate) for candidate in kmers(dna,len(kmer))])

def min_distance(kmer,dnastrs) :
    d = sum([min_distance1(kmer,dna) for dna in dnastrs])
    return d

def median_string(k, dnastrs) :

    pattern = None
    distance = sys.maxsize
    for kmer in itertools.product('ACGT',repeat=k) :
        kmer = ''.join(kmer)
        d = sum([min_distance1(kmer,dna) for dna in dnastrs])
        if d < distance :
            distance = d
            pattern = kmer

    return pattern


if __name__ == '__main__' :

    # dnastrs = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG', 'AGTTCGGGACAG' ]
    # assert median_string(3,dnastrs) == 'GAC'
    #

    # with open('Downloads/medium_string_data.txt','r') as f :
    #     f.readline()
    #     k = int(f.readline().strip())
    #     dnastrs = []
    #     while True:
    #         dna = f.readline().strip()
    #         if dna != 'Output' :
    #             dnastrs.append(dna)
    #         else :
    #             break
    #
    #     assert median_string(k,dnastrs) == 'CGGCGA'

    # with open('Downloads/dataset_158_9.txt','r') as f :
    #     k = int(f.readline().strip())
    #     dnastrs=[]
    #     while True:
    #         s = f.readline()
    #         if not s :
    #             break
    #         else :
    #             dnastrs.append(s)
    #
    #     print median_string(k,dnastrs)


    dnastrs = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC','GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
               'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG' ]
    print min_distance('TCTGAAG',dnastrs)
    print min_distance('ATAACGG', dnastrs)
    print min_distance('TAGTTTC', dnastrs)
    print min_distance('GTCAGCG', dnastrs)
    print min_distance('GGTTACT', dnastrs)
    print min_distance('GTAGGAA', dnastrs)

