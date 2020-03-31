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
    reach = {v:-1 for v in graph}
    low = {v:-1 for v in graph}
    visited = {v:False for v in graph}
    depth = 0
    bridges = []

    for vertex in graph:
        if not visited[vertex]:
            bridge_dfs(graph, vertex, vertex, reach, low, visited, bridges, depth)
    return bridges

def bridge_dfs(graph, u,v, reach, low, visited, bridges, depth):
    low[v] = depth
    reach[v] = depth
    visited[v] = True

    for edge in graph[v]:
        if edge != u:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                bridge_dfs(graph, v, edge, reach, low, visited, bridges, depth+1)
                low[v] = min(low[v], low[edge])
                if low[edge] > reach[v]:
                    bridges.append((v, edge))

def find_cycles(graph):
    visited = {v:False for v in graph}
    start = list(graph.keys())[-1]
    queue = [start]
    parent = start

    while queue:
        node = queue.pop(0)

        for edge in graph[node]:
            if parent != edge:
                if visited[edge]:
                    print(edge)
                    #return True
                if not visited[edge]:
                    queue.append(edge)
        visited[node] = True
        parent = node
    return False
print(find_bridges(graph))
print(find_cycles(graph))
