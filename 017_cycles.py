# This problem was asked by Pandora.
# 
# Given an undirected graph, determine if it contains a cycle.

graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
    5: [1]
}

def cycles(graph):
    visited = {v:False for v in graph}
    found = [False]
    cycle = []
    
    for vertex in graph:
        if visited[vertex] == False:
            dfs(graph, visited, vertex, vertex, found,cycle)
        # if found[0] == True:
        #     break
    return found[0], cycle
    
def dfs(graph, visited, u, v, found,cycle):
    # if found[0] == True:
    #     return
    visited[u] = True
    
    for edge in graph[u]:
        if visited[edge] and u != v:
            found[0] = True
            cycle.append((u,v))
        if not visited[edge]:
            dfs(graph,visited,edge,u,found,cycle)
            
print(cycles(graph))