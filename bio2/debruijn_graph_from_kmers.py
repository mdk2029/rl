import base

def debruijn_graph_from_kmers(kmers) :

    nodes = dict()
    for kmer in kmers :
        prefix = kmer[:-1]
        if prefix not in nodes :
            nodes[prefix] = []
        suffix = kmer[1:]
        if suffix not in nodes :
            nodes[suffix] = []
        nodes[prefix].append(suffix)

    return nodes


def print_sorted(graph) :
    adj_list = []
    for k,v in graph.iteritems() :
        if len(v) != 0 :
            adj_list.append((k,v))
    for i in xrange(0,len(adj_list)) :
        adj_list[i] = (adj_list[i][0],sorted(adj_list[i][1]))

    adj_list = sorted(adj_list, key=lambda x : x[0])
    for tup in adj_list:
        print tup[0], ' -> ', ','.join(tup[1])

if __name__ == '__main__':
     #print_adjlist(debruijn_graph_from_kmers(['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']))
     with open('Downloads/dataset_200_8_out.txt', 'w') as fout:
        with open('Downloads/dataset_200_8.txt', 'r') as fin :
            kmers = []
            for line in fin:
                kmers.append(line.rstrip())

            d = debruijn_graph_from_kmers(kmers)
            for tup in d:
                fout.write('%s -> %s\n' % (tup[0],','.join(tup[1])))

