import base

''' graph is in adjacency list format. It is a dict of lists. so graph[vertex]
    is a list of adjacent nodes'''

def find_eulerian_cycle(graph) :
    #first find total number of edges
    tot_edges = sum(len(v) for (_,v) in graph.iteritems())

    ''' random walk from vertex till we can walk no more '''
    def find_sub_cycle(vertex, graph) :
        assert vertex is not None
        cycle = [vertex]
        while True:
            neighbors = graph[vertex]
            if neighbors :
                next = neighbors[0]
                cycle.append(next)
                del neighbors[0]
                vertex = next
            else :
                assert cycle[0] == cycle[-1]
                return cycle

    def find_next_start_vertex(cycle, graph) :
        for v in cycle :
            if graph[v] :
                assert v != cycle[0]
                return v
        return None


    def splice(base_cycle, sub_cycle) :
        if not base_cycle :
            return sub_cycle
        for idx in xrange(0,len(base_cycle)) :
            if base_cycle[idx] == sub_cycle[0] :
                return base_cycle[0:idx] + sub_cycle + base_cycle[idx+1:]

        raise(Exception("cannot splice"))

    start_vertex = None
    for vertex in graph.iterkeys() :
        start_vertex = vertex
        break

    candidate_cycle = []
    while len(candidate_cycle) - 1 < tot_edges :
        if start_vertex is None :
            import pdb; pdb.set_trace()
        next_sub_cycle = find_sub_cycle(start_vertex,graph)
        candidate_cycle = splice(candidate_cycle,next_sub_cycle)
        start_vertex = find_next_start_vertex(candidate_cycle,graph)


    return candidate_cycle

def find_eulerian_path(graph) :

    #first calculate degrees of all nodes
    node_degs = {}

    def update_outdegree(nodes, node, odegree) :
        degrees = nodes.setdefault(node,[0,0])
        assert len(degrees) == 2
        degrees[1] = len(neighs)

    def update_indegree(nodes, node) :
        degrees = nodes.setdefault(node,[0,0])
        degrees[0] += 1

    for node,neighs in graph.iteritems() :
        update_outdegree(node_degs,node,len(neighs))
        for n in neighs :
            update_indegree(node_degs,n)


    #verify that there are exactly two terminal nodes
    start_candidates = []
    end_candidates = []
    for node,degs in node_degs.iteritems() :
        if degs[0] == degs[1] + 1 :
            end_candidates.append(node)
        elif degs[1] == degs[0] + 1 :
            start_candidates.append(node)

    assert len(start_candidates) == len(end_candidates) == 1

    start = start_candidates[0]
    end = end_candidates[0]

    #add an edge from end to start and remember it
    graph.setdefault(end,[]).append(start)

    #find eulerian cycle
    cycle = find_eulerian_cycle(graph)

    #locate edge end -> start
    for idx in xrange(0,len(cycle)-1) :
        if cycle[idx] == end and cycle[idx+1] == start :
            #found pivot point
            return cycle[idx+1:] + cycle[1:idx+1]

    return None



if __name__ == '__main__' :
     #graph = {0 :[3], 1 : [0], 2 : [1,6], 3 : [2], 4 : [2], 5 : [4], 6 : [5,8], 7 : [9], 8 : [7], 9 : [6]}
     #print find_eulerian_cycle(graph)

     #graph =  {0: [2], 1:[3], 2:[1], 3:[0,4], 6:[3,7], 7:[8], 8:[9], 9:[6]}
     #print find_eulerian_path(graph)

     graph = {}
     with open('Downloads/dataset_203_6.txt','r') as fin :
         for line in fin :
            line = line.strip()
            v_neigh = line.split("->")
            assert len(v_neigh) == 2
            vertex = int(v_neigh[0])
            neighs = map(int,v_neigh[1].split(','))
            assert not graph.has_key(vertex)
            assert len(neighs) >= 1
            graph[vertex] = neighs

     #cycle = find_eulerian_cycle(graph)
     path = find_eulerian_path(graph)
     with open('Downloads/dataset_203_2_out.txt','w') as fout :
         fout.write('->'.join(str(n) for n in path))

     # with open('Downloads/eulerian_path.txt','r') as fin :
     #     fin.readline()
     #     for line in fin :
     #         if line.find()
     #         line = line.strip()
     #         v_n = line.split("->")
     #         assert len(v_n) == 2
     #         vertex = int(v_n[0])
     #         neighs = map(int,v_n[1].split(','))
     #         assert not graph.has_key(vertex)
     #         assert len(neighs) >= 1
     #         graph[vertex] = neighs
     #






