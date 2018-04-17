import base

from debruijn_graph import debruijn_graph_from_kmers
from eulerian_cycle import find_eulerian_path


if __name__ == '__main__' :

    #kmers = ['CTTA','ACCA','TACC','GGCT','GCTT','TTAC']

    kmers = []

    with open('Downloads/dataset_203_7.txt','r') as fin:
        kmers = []
        fin.readline()
        for kmer in fin :
            kmers.append(kmer.rstrip())

    adj_list = debruijn_graph_from_kmers(kmers)

    graph = {}
    for elem in adj_list :
        graph[elem[0]] = elem[1]

    cycle = find_eulerian_path(graph)

    cycle = cycle[0] + ''.join(cycle[idx][-1] for idx in xrange(1,len(cycle)))

    with open('Downloads/dataset_203_7_out.txt','w') as fout:
        fout.write(cycle)



