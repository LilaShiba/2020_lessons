import heapq

# pipes = {
#     'plant': {'A': 1, 'B': 5, 'C': 20},
#     'A': {'C': 15},
#     'B': {'C': 10},
#     'C': {}
# }
#
# def least_cost(pipes):
#     seen = set()
#     distance = {} ; parent = {}
#     heap = [(0,('plant', 'plant'))]
#     heapq.heapify(heap)
#     vertice = pipes.keys()
#
#     while len(seen) < len(vertice):
#         cost, edge = heapq.heappop(heap)
#         u,v = edge
#         if v not in seen:
#             seen.add(v)
#             if cost < distance.get(v, float('inf')):
#                 distance[v] = cost
#                 parent[v] = u
#
#             for neighbor, cost in pipes[v].items():
#                 heapq.heappush(heap,(cost,(v,neighbor)))
#
#     path = {v:[] for v in vertice}
#     for u,v in parent.items():
#         path[v].append(u)
#     return path
# print(least_cost(pipes))

graph = {
    0: [2],

    2: [3],
    3: [0],

}

"""
2 --- 0 --- 1 --- 5
  \   |
   \  |
      3 --- 4
"""


# def find_cycles(graph):
#     cycles = []
#     visited = {v:False for v in graph}
#     for vertex in graph:
#         if not visited[vertex]:
#             stack = [vertex]
#             while stack:
#                 node = stack.pop()
#                 visited[node] = True
#                 for edge in graph[node]:
#                     if visited[edge]:
#                         return True
#                     else:
#                         stack.append(edge)
#
#     return cycles
#
# def bfs(graph, vertex, visited, cycles):
#     cache = {v:False for v in graph}
#     stack = [vertex]
#     while stack:
#         node = stack.pop()
#         cache[node] = True
#         visited[node] = True
#         # # if cycle
#         if cache[node]:
#             cycles.append(node)
#             break
#         # keep searching
#         for edge in graph[node]:
#             stack.append(edge)
#     return cycles
# print(find_cycles(graph))
# #print(bfs(graph,0))
#
# def make_edges_list(graph):
#     edges = []
#     for v in graph:
#         for u in graph[v]:
#             edges.append((u,v))
#     edges = sorted(edges, key=lambda x:x)
#     return edges

# import random, pprint
#
# matrix = [[random.randint(0,10) for x in range(5)]for y in range(5)]
#
# def bfs(maze,start,end):
#     visited = []
#     queue = [[start]]
#
#     while queue:
#         path = queue.pop(0)
#         node = path[-1]
#         x,y = node
#
#         if maze[x][y] == end:
#             return path
#
#         if node not in visited:
#             visited.append(node)
#             for cx, cy in (x+1, y), (x-1, y), (x,y-1), (x,y+1):
#                 if 0<= cx < len(maze) and 0 <= cy < len(maze[0]):
#                     new_path = list(path)
#                     new_path.append((cx,cy))
#                     queue.append(new_path)
#     return False
#
# if __name__ == "__main__":
#     path = bfs(matrix,(0,0), 5)
#     if path:
#         for u,v in path:
#             matrix[u][v] = 'x'
#         pprint.pprint(matrix)
