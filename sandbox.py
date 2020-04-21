

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


graph2 = {
            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

def bellman_ford(graph, start):
    cost = {key:float('inf') for key in graph}
    cost[start] = 0

    for vertex in range(len(graph)-1):
        for u in graph:
            for v,w in graph[u].items():
                if cost[u] != float('inf') and cost[u] + w < cost[v]:
                    cost[v] = cost[u] + w

    for u in graph:
        for v,w in graph[u].items():
            if cost[u] != float('inf') and cost[u] + w < cost[v]:
                return 'Neg Cycle at '+u+" and "+v
    return cost

print(bellman_ford(graph2, 't'))


def bf(graph, start):
    cost = {key:float('inf') for key in graph}
    cost[start] = 0

    for vertex in range(len(graph)-1):
        for u in graph:
            for v,w in graph[u].items():
                if cost[u] != float('inf') and cost[u] + w < cost[v]:
                    cost[v] = cost[u]+w

    for u in graph:
        for v,w in graph[u].items():
            if cost[u] != float('inf') and cost[u] + w < cost[v]:
                return "Shit, neg cycle at ", u, "and ", v

print(bf(graph2,'a'))


def get_edges(graph):
    low = reach = {v:float('inf') for v in graph}
    visited = {v:False for v in graph}
    depth = 0
    edges = []

    for vertex in graph:
        if not visited[vertex]:
            dfs(graph,vertex,vertex,low,reach,visited,edges,depth)
    return edges

def dfs(graph, u, v, low, reach, visited, edges, depth):
    low[v] = depth
    reach[v] = depth
    visited[v] = True

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph,v,edge,low,reach,visited,edges,depth+1)
                low[v] = min(low[v], low[edge])
                if reach[v] < low[edge]:
                    edges.append(edge)

print(get_edges(graph))

def bsearch(arr, target):
    lo, hi = 0, len(arr)-1

    while lo <= hi:
        mid = (lo+hi)//2
        if target == arr[mid]:
            return mid, arr[mid]
        elif target > arr[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


import random
arr = [random.randint(0,100) for x in range(100)]
arr = sorted(arr, key=lambda x:x)
print(bsearch(arr, 12))
