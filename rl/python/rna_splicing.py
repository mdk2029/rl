import fasta
import base
import bio2.protein_coding as pc
import re

if __name__ == '__main__' :

    dna = ''
    introns=[]

    with open('Downloads/rosalind_splc.txt', 'r') as fin:
        nl = fasta.NextLine(fin)
        id,dna = fasta.get_next_fasta_input(nl)
        assert id
        while True:
            id,inp = fasta.get_next_fasta_input(nl)
            if not id :
                break
            introns.append(inp)

    print dna
    print introns

    regex = '|'.join(introns)

    dna = re.sub(regex,'',dna)

    rna = base.dna_to_rna(dna)

    with open('Downloads/rosalind_splc_out.txt', 'w') as fout:
        fout.write(pc.peptide(rna))
        fout.write('\n')

