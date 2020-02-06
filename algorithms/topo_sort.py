def dfs(node, adj_list, cache):
    if node not in cache:
        cache.append(node)
        for edge in adj_list[node]:
            dfs(edge,adj_list,cache)
    return cache
    
def topo_sort(adj_list,cache):
    order = []
    for vertex in adj_list:
        dfs(vertex, adj_list, cache)
    return cache
    

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
        
        

print(topo_sort(graph, []))