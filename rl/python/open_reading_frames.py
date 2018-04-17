
import base
import bio2.protein_coding as pc
import fasta

def is_start_codon(codon) :
    return codon == 'AUG'

def is_end_codon(codon) :
    return codon == 'UAG' or codon == 'UGA' or codon == 'UAA'

def codons(rna) :
    idx = 0
    while(idx <= len(rna)-3) :
        yield rna[idx:idx+3]
        idx = idx + 3

if __name__ == '__main__' :

    aminos = set()

    with open('Downloads/rosalind_orf.txt','r') as fin :
        nl = fasta.NextLine(fin)

        _,dna = fasta.get_next_fasta_input(nl)
        dnas = [dna[idx:] for idx in (0,1,2)]
        dnas = dnas + [base.complement(dna)[idx:] for idx in (0,1,2)]

        for d in dnas :
            r = base.dna_to_rna(d)
            active_aminos = []
            for c in codons(r):
                if is_end_codon(c) :
                    for a in active_aminos :
                        aminos.add(a)
                    active_aminos = []
                else :
                    for idx in xrange(0,len(active_aminos)) :
                        active_aminos[idx] += pc.amino(c)
                    if is_start_codon(c) :
                        active_aminos.append(pc.amino(c))

            active_aminos = []

    with open('Downloads/rosalind_orf_out.txt','w') as fout :

        for a in aminos :
            fout.write(a)
            fout.write('\n')