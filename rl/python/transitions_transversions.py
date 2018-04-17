import fasta

def is_transition(amino1,amino2) :
    return  ( (amino1 == 'A' and amino2 == 'G') or
                (amino1 == 'G' and amino2 == 'A') or
                    (amino1 == 'C' and amino2 == 'T') or
                        (amino1 == 'T' and amino2 == 'C'))

def is_transversion(amino1,amino2) :
    return ( (amino1 != amino2) and (not is_transition(amino1,amino2)))



if __name__ == '__main__' :

    with open('Downloads/rosalind_tran.txt','r') as fin:

        nl = fasta.NextLine(fin)
        id1,dna1 = fasta.get_next_fasta_input(nl)
        assert id1
        id2,dna2 = fasta.get_next_fasta_input(nl)
        assert id2

        transition_count = 0
        transversion_count = 0

        assert len(dna1) == len(dna2)
        for a1,a2 in zip(dna1,dna2) :
            if is_transition(a1,a2) :
                transition_count += 1
            elif a1 != a2 :
                transversion_count += 1

        print float(transition_count)/float(transversion_count)

