from operator import itemgetter
import fasta

def gc_percentage(dna) :
    cg = 0.0
    for c in dna :
        if c.upper() == 'C' or c.upper() == 'G' :
            cg = cg + 1
    return 100.0 * cg / len(dna)

if __name__ == '__main__' :
    inputs = []
    with open('Downloads/rosalind_gc.txt','r') as fin :
        nl = fasta.NextLine(fin)
        while(True) :
            id,dna = fasta.get_next_fasta_input(nl)
            if not id:
                break
            else :
                inputs.append((id,dna))

    cg_contents = [(id,gc_percentage(dna)) for id,dna in inputs]
    max_content = max(cg_contents,key=itemgetter(1))
    print max_content[0]
    print max_content[1]

