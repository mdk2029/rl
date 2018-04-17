import fasta

class Node(object) :
    def __init__(self,id,dna):
        self.id = id
        self.dna = dna

    def __str__(self):
        return self.id

    def overlaps_with(self,node2,k):
        return self.dna[-k:] == node2.dna[:k]


if __name__ == '__main__':
    nodes = []
    k = 3
    with open('Downloads/rosalind_grph.txt','r') as fin:
        nl = fasta.NextLine(fin)
        while True:
            id,dna = fasta.get_next_fasta_input(nl)
            if not id :
                break
            else :
                nodes.append(Node(id,dna))

    all_edges = [(str(n1),str(n2)) for n1 in nodes for n2 in nodes if n1 != n2 and n1.overlaps_with(n2,3)]

    with open('Downloads/rosalind_grph_out.txt','w') as fout :
        for e in all_edges :
            fout.write('%s %s'%(e[0],e[1]))
            fout.write('\n')



