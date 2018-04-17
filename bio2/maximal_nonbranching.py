import base
import networkx as nx
from itertools import ifilter
from debruijn_graph import debruijn_graph_from_kmers
from all_eulerian_cycles import Node,adjlist_nxmultidigraph

def maximal_nonbranchingpaths(graph) :

    assert isinstance(graph,nx.MultiDiGraph)

    def is_simple_node(graph,n) :
        return graph.in_degree(n) == 1 and graph.out_degree(n) == 1

    non_branching_paths = []

    for node in graph.nodes() :
        if not is_simple_node(graph,node) :
            for edge in graph.out_edges(node) :
                nb = [edge]
                w = nb[-1][1]
                while is_simple_node(graph, w) :
                    u = graph.neighbors(w)[0]
                    nb.append((w,u))
                    w = u

                non_branching_paths.append(nb)

    return non_branching_paths

if __name__ == '__main__' :

    # g = nx.MultiDiGraph()
    # g.add_edges_from([('AT','TG'),('AT','TG'),('AT','TG'),('TA','AA'),('AA','AT'),('TG','GT'),('GT','TT'),('TG','GC'),('GC','CC'),('CC','CA'),('CA','AT'),('GA','AT'),('GG','GA'),('GG','GG'), ('TG','GG')])

    #kmers = [ 'ATG','ATG','TGT','TGG','CAT','GGA','GAT','AGA']
    kmers = []
    with open('Downloads/dataset_205_5.txt','r') as fin :
        for line in fin:
            kmers.append(line.strip())

    d = debruijn_graph_from_kmers(kmers)

    graph = adjlist_nxmultidigraph(d)

    paths = maximal_nonbranchingpaths(graph)

    def print_edge(p) :
        pstr = ''
        for index,edge in enumerate(p) :
            if index == 0 :
                pstr = str(edge[0]) + str(edge[1])[-1]
            else :
                pstr += str(edge[1])[-1]
        return pstr

    paths = sorted(map(print_edge,paths))

    with open('Downloads/dataset_205_5_out.txt','w') as fout:
        for p in paths :
            fout.write(p)
            fout.write('\n')





