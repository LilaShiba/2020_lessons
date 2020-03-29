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
    cycle_start = []

    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, visited, vertex, vertex, found, cycle_start)
        if found[0]:
            return cycle_start
    return cycle_start

def dfs(graph, visited, u, v, found, cycle_start):
    if found[0]:
        return cycle_start

    visited[u] = True

    for edge in graph[u]:
        if visited[edge] and u != v:
            cycle_start.append(edge)
            print(cycle_start)
            found[0] = True
            return
        if not visited[edge]:
            dfs(graph,visited,edge,u,found, cycle_start)


print(cycles(graph))
