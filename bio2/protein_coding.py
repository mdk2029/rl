import base

genetic_code = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVVZYZYSSSSZCWCLFLF'

def is_stop(amino) :
    return amino == 'Z'

def amino(codon):
    return genetic_code[base.patternToNumber(codon)]

def peptide(amino_sequence, bailOnStop=True) :

    peptide = ''

    for idx in xrange(0,len(amino_sequence),3) :
        if idx + 3 > len(amino_sequence) :
            break
        codon = amino_sequence[idx:idx+3]
        amino = genetic_code[base.patternToNumber(codon)]
        if is_stop(amino) and bailOnStop:
            return peptide
        else :
            peptide += amino

    return peptide


def peptide_encoding(pep,rna) :
    whole_translation = peptide(rna,bailOnStop=False)
    plen = len(pep)
    locations = []
    for idx in xrange(0,len(whole_translation)-plen + 1) :
        if whole_translation[idx:idx+plen] == pep :
            locations.append(idx*3)
    return locations

def encoding_locations(pep,dna) :

    plen = len(pep)

    #non_reversed_complement = base.complement(dna)[::-1]

    locations = set()

    rna_1 = base.dna_to_rna(dna)

    for l in peptide_encoding(pep,rna_1) :
        locations.add(l)

    rna_2 = rna_1[1:]
    for l in peptide_encoding(pep,rna_2):
        locations.add(l+1)

    rna_3 = rna_1[2:]
    for l in peptide_encoding(pep,rna_3) :
        locations.add(l+2)

    rna_4 = base.dna_to_rna(base.complement(dna))
    for l in peptide_encoding(pep,rna_4):
        locations.add(len(dna)-(l+3*plen-1+1))

    rna_5 = rna_4[1:]
    for l in peptide_encoding(pep,rna_5):
        locations.add(len(dna)-(l+1+3*plen-1+1))

    rna_6 = rna_4[2:]
    for l in peptide_encoding(pep,rna_6):
        locations.add(len(dna)-(l+2+3*plen-1+1))

    encoding_fragment = []
    for l in sorted(locations) :
        encoding_fragment.append(dna[l:l+3*plen])

    return encoding_fragment

if __name__ == '__main__':

    #ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA

    #print peptide('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA',bailOnStop=False)

    print peptide('CCUCGUACUGAUAUUAAU', bailOnStop=False)
    print peptide('CCUCGUACAGAAAUCAAC', bailOnStop=False)
    print peptide('CCCAGUACCGAGAUGAAU', bailOnStop=False)
    print peptide('CCCAGGACUGAGAUCAAU', bailOnStop=False)

    # with open('Downloads/protein_translation.txt'G,'r') as fin :
    #     fin.readline()
    #     amino_sequence = fin.readline().strip()
    #     fin.readline()
    #     expected_output = fin.readline().strip()
    #     our_output = peptide(amino_sequence)
    #     print our_output
    #     assert our_output == expected_output

    # with open('Downloads/dataset_96_4.txt','r') as fin :
    #     amino_sequence = fin.readline().strip()
    #     our_output = peptide(amino_sequence)
    #     print our_output

    #print encoding_locations('MA','ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA')

    # with open('Downloads/dataset_96_7.txt', 'r') as fin :
    #     with open('Downloads/dataset_96_7_out.txt', 'w') as fout :
    #         dna = fin.readline().strip()
    #         pep = fin.readline().strip()
    #         for op in encoding_locations(pep,dna) :
    #             fout.write(op)
    #             fout.write('\n')

