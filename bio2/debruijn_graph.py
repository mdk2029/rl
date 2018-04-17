import base

def debruijn_graph_from_text(text,k) :

    nodes = [(kmer,[]) for kmer in base.kmers(text,k-1)]
    for i in xrange(0,len(nodes)-1) :
        nodes[i][1].append(nodes[i+1][0])

    del nodes[-1]

    return debruijn_graph(nodes)

def debruijn_graph_from_kmers(kmers) :
    nodes = [ (kmer[0:-1], [kmer[1:]]) for kmer in kmers]
    return debruijn_graph(nodes)

def debruijn_graph_from_kmerpairs(kmerpairs):
    nodes = []
    for p in kmerpairs :
        prefix = p.split('|')[0][:-1] + '|' + p.split('|')[1][:-1]
        suffix = p.split('|')[0][1:] + '|' + p.split('|')[1][1:]
        nodes.append((prefix,[suffix]))
    return debruijn_graph(nodes)


#nodes is a list in [node,[neighbor]] format
def debruijn_graph(nodes) :

    nodes = sorted(nodes,key=lambda x : x[0])
    final_nodes = [(nodes[0][0], nodes[0][1])]
    del nodes[0]

    for node,neighbors in nodes :
        exists_in_final = False
        for fnode,fneighbors in final_nodes :
            if node == fnode :
                fneighbors += neighbors
                exists_in_final = True
                break
        if not exists_in_final :
            final_nodes.append((node,neighbors))

    #for idx in xrange(0,len(final_nodes)):
    #    print final_nodes[idx][0], " -> ", sorted(final_nodes[idx][1])

    retlist = [ (final_nodes[idx][0],sorted(final_nodes[idx][1])) for idx in xrange(0,len(final_nodes)) ]

    return retlist



if __name__ == '__main__' :

    d1 = debruijn_graph_from_text("AAGATTCTCTAAGA",4)
    for elem in d1 :
        print elem[0], " -> ", ','.join(elem[1])

    kmers = base.kmers("AAGATTCTCTAAGA",4)
    d2 = debruijn_graph_from_kmers(kmers)
    for elem in d2 :
        print elem[0], " -> ", ','.join(elem[1])



     # with open('Downloads/debruijn_out.txt', 'w') as fout:
     #    with open('Downloads/De_Bruijn_Graph_from_a_String.txt', 'r') as fin :
     #        inputline = fin.readline()
     #        k = int(fin.readline().rstrip())
     #        text = fin.readline().rstrip()
     #        outputline = fin.readline()
     #
     #        expected_output = [line.rstrip() for line in fin]
     #        our_output = [elem[0] + " -> " + ','.join(elem[1]) for elem in debruijn_graph(text,k)]
     #
     #        assert our_output == expected_output




    # with open('Downloads/dataset_199_6_out.txt', 'w') as fout:
    #     with open('Downloads/dataset_199_6.txt', 'r') as fin :
    #         k = int(fin.readline().rstrip())
    #         text = fin.readline().rstrip()
    #
    #         d = debruijn_graph(text,k)
    #         for elem in d :
    #             fout.write(elem[0] + " -> " + ','.join(elem[1]) + '\n')




