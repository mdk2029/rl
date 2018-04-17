import base
from eulerian_cycle import find_eulerian_cycle
from debruijn_graph import debruijn_graph_from_kmers

def binary_strings(k) :
    return ['{i:0>{k}b}'.format(i=i, k=k) for i in range(2**k)]

if __name__ == '__main__' :
    k = 8
    bs = binary_strings(k)

    adj_list = debruijn_graph_from_kmers(bs)

    graph = {}
    for elem in adj_list :
        graph[elem[0]] = elem[1]

    cycle = find_eulerian_cycle(graph)
    edges = []
    for idx in xrange(0,len(cycle)-1) :
        edges.append(cycle[idx] + (cycle[idx+1])[-1])

    idx = 0
    circular_k_universal = edges[idx]
    while(len(circular_k_universal) != 2**k) :
        idx += 1
        circular_k_universal += (edges[idx][-1])

    with open('Downloads/kuniversal_out_8.txt','w') as fout :
        fout.write(circular_k_universal)