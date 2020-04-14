
#
# def find_min_range(people, tower):
#     min_range = -1
#     towers = [-float('inf')] + sorted(tower) + [float('inf')]
#     for person in people:
#         idx = search(person, towers)
#         left = person - towers[idx-1]
#         right = towers[idx] - person
#
#         min_range = max(min_range, min(left, right))
#     return min_range
#
# def search(person, towers):
#     lo,hi= 0, len(towers)-1
#
#     while lo <= hi:
#         mid = (lo+hi)//2
#
#         if towers[mid] > person:
#             hi = mid -1
#         elif towers[mid] < person:
#             lo = mid +1
#         else:
#             return mid
#     return lo
#
# print(find_min_range(listeners, towers))


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

import random, pprint
matrix = [[random.randint(0,10) for x in range(5)] for y in range(5)]
pprint.pprint(matrix)

def get_neighbors(x,y,matrix,block):
    row = len(matrix)
    col = len(matrix[0])
    n = ((x+1,y), (x-1,y), (x,y-1), (x, y+1), (x-1,y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1))
    neighbors = ((x,y) for x,y in n if 0<= x < row and 0 <= y < col and matrix[x][y] < block)
    return neighbors

def bfs(graph,start,end):
    queue=[[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path

        x,y = node
        neighbors = get_neighbors(x,y,graph,100)
        for cx,cy in neighbors:
            if (cx,cy) not in visited:
                visited.append((cx,cy))
                new_list = list(path)
                new_list.append((cx,cy))
                queue.append(new_list)
    return False

print(bfs(matrix,(0,0), (4,4) ))

def bfs_adj(graph,start,end):
    visited = {v:False for v in graph}
    queue = [start]
    parent = {v:None for v in graph}
    parent[start]= start

    while queue:
        node = queue.pop(0)
        if node == end:
            while end != start:
                print(end)
                end = parent[end]
            print(end)

            return parent
        if not visited[node]:
            visited[node] = True
            for u in graph[node]:
                if parent[node] != u:
                    parent[u] = node
                queue.append(u)
    return False

print(bfs_adj(graph, 3, 5))
