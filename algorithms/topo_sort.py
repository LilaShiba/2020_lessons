def dfs(node, adj_list, cache,stack):
    cache.append(node)
    for edge in adj_list[node]:
        if edge not in cache:
            dfs(edge,adj_list,cache,stack)
    stack.append(node)
    
    
    
def topo_sort(adj_list,cache):
    order,stack = [], []
    for vertex in adj_list:
        if vertex not in cache:
            dfs(vertex, adj_list, cache,stack)
    return stack
    

graph = {0: [1, 2, 3], 1: [3], 2: [4], 3: [4, 0], 4: [0]}

        
        

print(topo_sort(graph, []))