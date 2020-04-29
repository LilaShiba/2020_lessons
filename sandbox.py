# def knapsack(weight, value, limit):
#     table = [0] * (limit+1)

#     for current_cut in range(1, limit+1):
#         max_cut = 0
#         for current_weight in range(1, len(weight)):
#             # if current weight <= current weight limit
#             if weight[current_weight] <= current_cut:
#                 current_value = value[current_weight]
#                 subproblem = current_value + table[current_cut - weight[current_weight]]
#                 max_cut = max(max_cut, subproblem)
#         table[current_cut] = max_cut
#     return table

# item_weights = [0, 2, 10, 3, 6, 18]
# item_values = [0, 1, 20, 3, 14, 100]

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
    low = reach = {v:float('inf') for v in graph}
    visited = {v:False for v in graph}
    depth = 0
    edges = []

    for v in graph:
        if not visited[v]:
            dfs(graph,v,v,low,reach,visited,edges,depth)
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
                dfs(graph, v, edge, low, reach, visited, edges, depth+1)
                low[v] = min(low[v], low[edge])
                if reach[v] < low[edge]:
                    edges.append(edge)

print(find_edges(graph))



# def get_edges(graph):
#     edges = []
#     depth = 0 
#     reach = low = {x:float('inf') for x in graph}
#     visited = {x:False for x in graph}

#     for vertex in graph:
#         if not visited[vertex]:
#             dfs_me(graph, vertex,vertex,reach,low,visited,edges,depth)
#     return edges

# def dfs_me(graph, u,v, reach, low, visited, edges, depth):
#     reach[v] = depth 
#     low[v] = depth 
#     visited[v] = True 

#     for edge in graph[v]:
#         if u != edge:
#             if visited[edge]:
#                 low[v] = min(low[v], reach[edge])
#             else:
#                 dfs_me(graph,v,edge,reach,low,visited,edges,depth+1)
#                 low[v] = min(low[v], low[edge])
#                 if reach[v] < low[edge]:
#                     edges.append(edge)


# arr = [1, 5, 8, 9, 10, 17, 17, 20]
# size = len(arr)
# ans = 22
# arr = [61, 90, 85, 19, 20, 96, 75, 20, 28, 13, 93, 88, 8, 35, 59]
# ans = True
