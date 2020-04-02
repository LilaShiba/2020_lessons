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

def find_edges(graph):
    reach = {v:-1 for v in graph}
    low = {v:-1 for v in graph}
    visited = {v:False for v in graph}
    depth = 0
    edges = []

    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, vertex, reach, low, visited, depth, edges)
        return edges

def dfs(graph, u, v, reach, low, visited, depth, edges):
    reach[v] = depth
    low[v] = depth
    visited[v] = True

    for edge in graph[v]:
        if edge != u:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph, v, edge, reach, low, visited, depth+1, edges)
                low[v] = min(low[v], low[edge])
                if low[edge] > reach[v]:
                    edges.append(edge)

edges = find_edges(graph)
print("Edges:",edges)
cycle = graph.keys() - edges
print("Cycles:",cycle)
