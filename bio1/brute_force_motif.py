from base import hamming_neighborhood,hamming_distance,kmers
import sys

def appears(pattern, dna, d) :
    plen = len(pattern)
    for candidate in kmers(dna,plen):
        if hamming_distance(pattern,candidate) <=d :
            return True
    return False

def brute_force_motif_search(dnaset, k, d) :

    motifs = set()
    for dna in dnaset :
        others = dnaset - {dna}
        for candidate in kmers(dna,k):
            for hneighbor in hamming_neighborhood(candidate,d) :
                if all([appears(hneighbor,o, d) for o in others]) :
                    motifs.add(hneighbor)

    return motifs


if __name__ == '__main__' :

    #dnaset = { 'ATTTGGC', 'TGCCTTA','CGGTATC', 'GAAAATT' }

    dnaset = { 'TTCCGTGTAGAGGTAGGGCCGTGCA', 'TACTGCCAGTTTTAAGGGCCCGTTT', 'TCTCGCTAATGGGACCAGCGTAGGT', 'CGAAAGTTCGCCCGTGGGCCTTTGG',
               'GGGGCCCTATGGCTAACGGAAGGGA', 'AACTGAGCAGGAATCGGGACATGCC'}

    motifs = sorted(brute_force_motif_search(dnaset,5,1))
    map(lambda x : sys.stdout.write("%s " % x), motifs)

    # print hamming_distance('ACC','ATT')