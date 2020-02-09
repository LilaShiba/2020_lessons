graph = {        
            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }
            

def bellman_ford(graph, start):
    # create dist hash
    # set all vertices to inf except start
    dist = {vertex:float('inf') for vertex in graph}
    dist[start] = 0
    unseenNodes = graph
    vertices = [v for v in graph]
    # cycle graph and relax edges
    # do this for every vertex
    for u in range(len(graph)-1):
        for vertex in graph:
        #vertex = vertices[u]
            for v,w in graph[vertex].items():
                if dist[vertex] != float('inf') and dist[vertex] + w < dist[v]:
                    dist[v] = w + dist[vertex]
        
    # check for neg edges
    
    for vertex in unseenNodes:
        for v,w in graph[vertex].items():
            if dist[vertex] != float('inf') and dist[vertex] + w < dist[v]:
                return "Negitive Cycle from", vertex, 'to', v
    
    return dist

print(bellman_ford(graph, 'c'))