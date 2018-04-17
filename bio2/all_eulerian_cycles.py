import base
import networkx as nx
from itertools import ifilter
from debruijn_graph import debruijn_graph_from_kmerpairs

class Node :
    def __init__(self,kmer,start=False):
        self.kmer = kmer
        self.start = start

    def __str__(self) :
        return self.kmer

    def __repr__(self):
        return self.kmer


def adjlist_nxmultidigraph(adj_list) :
    graph = nx.MultiDiGraph()
    nodedict = {}
    for elem in adj_list :
        nodedict.setdefault(elem[0], Node(elem[0]))
        for n in elem[1] :
            graph.add_edge(nodedict[elem[0]], nodedict.setdefault(n,Node(n)))

    return graph


def in_degree(g,n) :
    indegree = 0
    for vertex in g :
        if n in g.neighbors(vertex) :
            indegree += 1
    return indegree

def out_degree(g,n):
    return len(g.neighbors(n))

def is_simple(g) :
    for vertex in g :
        if in_degree(g,vertex) > 1 :
            return False
    return True

def all_eulerian_cycles(g,start=None) :
    if not isinstance(g,nx.MultiDiGraph) :
        raise Exception("expect nx.MultiDiGraph")
    if not nx.euler.is_eulerian(g) :
        raise Exception("g is not eulerian")

    all_graphs = set([g])
    while True:
        tosimplify_g = next(ifilter(lambda gr : not is_simple(gr), all_graphs),None)
        if not tosimplify_g :
            break
        multivertex = next(ifilter(lambda v : in_degree(tosimplify_g,v) > 1,tosimplify_g.nodes()),None)
        assert multivertex

        for incoming in tosimplify_g.in_edges(multivertex) :
            for outgoing in tosimplify_g.out_edges(multivertex) :
                #modify simplify_g to add the bypass edge

                newvertex = Node(multivertex.kmer)
                tosimplify_g.add_edge(incoming[0],newvertex)
                tosimplify_g.add_edge(newvertex,outgoing[1])
                tosimplify_g.remove_edge(*incoming)
                tosimplify_g.remove_edge(*outgoing)

                simplified = tosimplify_g.copy()
                if nx.is_strongly_connected(simplified) :
                    all_graphs.add(simplified)
                #else :
                    #print "not sc : ", simplified.edges()

                #revert all modifications
                tosimplify_g.add_edge(*outgoing)
                tosimplify_g.add_edge(*incoming)
                tosimplify_g.remove_edge(newvertex,outgoing[1])
                tosimplify_g.remove_edge(incoming[0],newvertex)
                assert len(tosimplify_g.in_edges(newvertex)) == 0
                assert len(tosimplify_g.out_edges(newvertex)) == 0
                tosimplify_g.remove_node(newvertex)

        all_graphs.remove(tosimplify_g)

    for g in all_graphs :
        assert nx.euler.is_eulerian(g)

        start = next(ifilter(lambda n : n.start==True,g.nodes()),None)
        assert start != None
        yield nx.euler.eulerian_circuit(g,start)

if __name__ == '__main__' :

    graph = nx.MultiDiGraph()

    with open('Downloads/dataset_204_15.txt','r') as fin :
        kd = fin.readline().strip()
        k = int(kd.split()[0])
        d = int(kd.split()[1])
        kmerpairs = []
        for line in fin :
            line = line.strip()
            kmerpairs.append(line.strip())

    # kmerpairs = ['AAT|CCA','ATG|CAT','ATG|GAT','CAT|GGA','CCA|GGG','GCC|TGG', 'GGA|GTT','GGG|TGT','TAA|GCC','TGC|ATG','TGG|ATG']
    # k = 3
    # d = 1

    adj_list = debruijn_graph_from_kmerpairs(kmerpairs)

    graph = adjlist_nxmultidigraph(adj_list)

    # nodedict = {}
    # for elem in adj_list :
    #     nodedict.setdefault(elem[0], Node(elem[0]))
    #     for n in elem[1] :
    #         graph.add_edge(nodedict[elem[0]], nodedict.setdefault(n,Node(n)))

    #print graph
    #for e in graph.edges() :
    #    print e[0], '->' , e[1]


    #find the two terminal nodes
    start = []
    end = []
    for n in graph :
        if graph.in_degree(n) == 0 :
            start.append(n)
        if graph.out_degree(n) == 0 :
            end.append(n)

    assert len(start) == 1
    assert len(end) == 1

    start[0].start = True
    graph.add_edge(end[0],start[0])

    paths = set()
    for circuit in all_eulerian_cycles(graph,start) :
        prefixpath = None
        suffixpath = None

        for edge in circuit :
            pairs = str(edge[0]).split('|')
            if prefixpath is None :
                prefixpath = pairs[0]
                suffixpath = pairs[1]
            else :
                prefixpath += pairs[0][-1]
                suffixpath += pairs[1][-1]

        paths.add((prefixpath,suffixpath))

    with open('Downloads/dataset_204_15_out.txt','w') as fout :
        for p in paths :
            if prefixpath[k+d:] == suffixpath[0:-(k+d)] :
                p = prefixpath[0:k+d] + prefixpath[k+d:] + suffixpath[-(k+d):]
                fout.write(p)
                fout.write('\n')












