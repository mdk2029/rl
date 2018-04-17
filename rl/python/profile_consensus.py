import fasta
from collections import Counter

def profile(dnas) :

    dna_len = len(dnas[0])
    num_strs = len(dnas)

    pro = [[0] * dna_len for i in xrange(4)]

    for d in dnas :
        for idx,c in enumerate(d) :
            pro['ACGT'.find(c)][idx] += 1

    return pro

def consensus_string(profile_matrix) :
    assert len(profile_matrix) == 4

    consensus = ''
    dna_len = len(profile_matrix[0])
    for pos in xrange(dna_len) :
        next = None
        curr_max = 0
        for idx in xrange(4) :
            if not next or profile_matrix[idx][pos] > curr_max :
                curr_max = profile_matrix[idx][pos]
                next = 'ACGT'[idx]
        consensus += next

    return consensus


if __name__ == '__main__' :

    dnas = []
    with open('Downloads/rosalind_cons.txt','r') as fin :
        nl = fasta.NextLine(fin)
        while True:
            id,dna = fasta.get_next_fasta_input(nl)
            if id is None :
                break
            dnas.append(dna)

    assert all([len(d) == len(dnas[0]) for d in dnas])

    with open('Downloads/rosalind_cons_out.txt','w') as fout :
        pro = profile(dnas)
        fout.write(consensus_string(pro))
        fout.write('\n')
        for idx,c in enumerate('ACGT') :
            fout.write('%s: %s'%(c,' '.join([str(i) for i in pro[idx]])))
            fout.write('\n')







