import disjoint_set

def connected_components(num_nodes,edges) :

    ds = disjoint_set.DisjoinSet(num_nodes)
    for e in edges :
        ds.merge(e[0],e[1])

    num_cc = set()
    for v in xrange(num_nodes) :
        num_cc.add(ds.find(v))

    return len(num_cc)


if __name__ == '__main__' :

    with open('Downloads/rosalind_tree.txt','r') as fin :
        num_nodes = int(fin.readline().strip())
        edges = []
        for line in fin :
            edge = map(int,line.split())
            edges.append((edge[0]-1,edge[1]-1)) #vertices in problem start with 1


    num_cc = connected_components(num_nodes,edges)

    print num_cc - 1



