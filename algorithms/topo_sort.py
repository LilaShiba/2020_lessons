def dfs(node, adj_list, cache,stack):
    cache.append(node)
    for edge in adj_list[node]:
        if edge not in cache:
            dfs(edge,adj_list,cache,stack)
    stack.insert(0,node)



def topo_sort(adj_list,cache):
    order,stack = [], []
    for vertex in adj_list:
        if vertex not in cache:
            dfs(vertex, adj_list, cache,stack)
    return stack


graph = {0: [1, 2, 3], 1: [3], 2: [4], 3: [4, 0], 4: [0]}
graph2 = {
        1: [2, 3],
        2: [4, 5, 6],
        3: [4,6],
        4: [5,6],
        5: [6],
        6: []
    }
# [ 0, 1, 3, 4, 2 ]

def dfs_topo(graph):
    visited = set()
    stack = []

    for v in graph:
        if v not in visited:
            dfs_sort(v, visited, stack, graph)
    return stack 

def dfs_sort(v,visited,stack,graph):
    visited.add(v)
    for edge in graph[v]:
        if edge not in visited:
            dfs_sort(edge,visited,stack,graph)
    stack.insert(0,v)




print(topo_sort(graph2, []))
print(dfs_topo(graph2))