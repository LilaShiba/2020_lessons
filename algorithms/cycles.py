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

d_graph = {
           0:[2],
           1:[0],
           2:[3],
           3:[0],
           4:[3],
           5:[1]
}

def find_cycle(graph):
    discover = {v:False for v in graph}
    found = [False]

    for vertex in graph:
        if not discover[vertex]:
            dfs_visit(graph, vertex, discover, vertex, found)
        if found[0]:
            break
    return found[0]

def dfs_visit(adj,u,discover,prev_node,found):
    if found[0]:
        return
    discover[u] = True
    for v in adj[u]:
        if discover[v] and v != prev_node:
            found[0] = True
            return
        if not discover[v]:
            dfs_visit(adj, v, discover, u, found)

def bfs_cycle(graph):
    seen = {v:False for v in graph}
    start = list(graph.keys())[0]
    queue = [start]
    parent = start

    while queue:
        node = queue.pop()
        seen[node] = True
        for edge in graph[node]:
            if edge != parent:
                if seen[edge]:
                    print(edge)
                    return
                if not seen[edge]:
                    queue.append(edge)


        parent = node
    return False


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
    cycles = graph.keys() - edges
    true_cycles = []
    for x in cycles:
        if len(graph[x]) > 0:
            true_cycles.append(x)

    return true_cycles

print(find_all_in_cycle(graph))
