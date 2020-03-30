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

    while queue:
        node = queue.pop(0)
        if not seen[node]:
            seen[node] = True
            for edge in graph[node]:
                if seen[edge]:
                    return True
                queue.append(edge)
    return False

print(find_cycle(graph))
print(bfs_cycle(graph))
