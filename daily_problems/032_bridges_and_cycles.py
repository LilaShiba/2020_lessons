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
                # is reach of edge lower than parent low?
                low[v] = min(low[v], reach[edge])
            else:
                # keep searching
                dfs(graph, v, edge, visited, low, reach, edges, depth+1)
                # when you can't search any more
                # change parent low to be the lowest
                low[v] = min(low[v], low[edge])
                # if parent reach is less than child low
                # that edge isn't connected to another path
                if low[edge] > reach[v]:
                    edges.append(edge)


def find_all_in_cycle(graph):
    edges = find_bridges(graph)
    print('Edges:', edges)
    cycles = graph.keys() - edges
    return cycles

print('Cycles:', find_all_in_cycle(graph))
