import unittest
# https://cp-algorithms.com/graph/bridge-searching.html
graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
    5: [1]
}

"""
2 --- 0 --- 1 --- 5
  \   |
   \  |
      3 --- 4
"""
# https://cp-algorithms.com/graph/bridge-searching.html
graph = {
    0: [1, 2, 3],
    1: [0, 5],
    2: [0, 3],
    3: [0, 2, 4],
    4: [3],
    5: [1]
}

"""
2 --- 0 --- 1 --- 5
  \   |
   \  |
      3 --- 4
"""

def find_bridges(graph):
    visited = {v:False for v in graph}
    low = {v:-1 for v in graph}
    reach = {v:-1 for v in graph}
    depth = 0
    edges = []
    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, vertex, visited, low, reach, edges, depth)
    return edges

def dfs(graph, u, v, visited, low, reach, edges, depth):
    visited[v] = True
    low[v] = depth
    reach[v] = depth

    for edge in graph[v]:
        if edge != u:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph, v, edge, visited, low, reach, edges, depth+1)
                low[v] = min(low[v], low[edge])
                if low[edge] > reach[v]:
                    edges.append(edge)


def find_all_in_cycle(graph):
    edges = find_bridges(graph)
    print('Edges:', edges)
    cycles = graph.keys() - edges
    true_cycles = []
    for x in cycles:
        if len(graph[x]) > 0:
            true_cycles.append(x)

    return true_cycles

print('Cycles:', find_all_in_cycle(graph))
