def knapsack(weight, value, limit):
    table = [0] * (limit+1)

    for current_cut in range(1, limit+1):
        max_cut = 0
        for current_weight in range(1, len(weight)):
            # if current weight <= current weight limit
            if weight[current_weight] <= current_cut:
                current_value = value[current_weight]
                subproblem = current_value + table[current_cut - weight[current_weight]]
                max_cut = max(max_cut, subproblem)
        table[current_cut] = max_cut
    return table

item_weights = [0, 2, 10, 3, 6, 18]
item_values = [0, 1, 20, 3, 14, 100]

# s = 'babad'

# def longest_pal(s):
#     longest = ''
#     for x in range(len(s)):
#         for y in range(len(s)):
#             print(s[x:y+1])

# print(longest_pal('abbb'))


def knapsack(weights, values, limit):
    table = [[0 for _ in range(limit+1)]for _ in range(len(weights))]

    for cut in range(1, len(weights)):
        for current_limit in range(1, limit+1):
            current_weight = weights[cut]
            current_value = values[cut]
            if current_weight <= current_limit:
                table[cut][current_limit] = max(table[cut-1][current_limit-current_weight] + current_value, table[cut-1][current_limit])
            else:
                table[cut][current_limit] = table[cut-1][current_limit]
    return table


import pprint
pprint.pprint(knapsack(item_weights, item_values, 15))




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

def get_edges(graph):
    edges = []
    depth = 0 
    reach = low = {x:float('inf') for x in graph}
    visited = {x:False for x in graph}

    for vertex in graph:
        if not visited[vertex]:
            dfs_me(graph, vertex,vertex,reach,low,visited,edges,depth)
    return edges

def dfs_me(graph, u,v, reach, low, visited, edges, depth):
    reach[v] = depth 
    low[v] = depth 
    visited[v] = True 

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs_me(graph,v,edge,reach,low,visited,edges,depth+1)
                low[v] = min(low[v], low[edge])
                if reach[v] < low[edge]:
                    edges.append(edge)



def find_edges(graph):
    reach = low = {v:float('inf') for v in graph}
    visited = {v:False for v in graph}
    depth = 0
    edges = []

    for v in graph:
        if not visited[v]:
            dfs_edge(graph, v,v, reach,low,visited,edges,depth)
    return edges 

def dfs_edge(graph, u, v, reach, low, visited, edges, depth):
    reach[v] = depth 
    low[v] = depth 
    visited[v] = True

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs_edge(graph, v, edge, reach, low, visited, edges, depth+1)
                low[v] = min(low[v], low[edge])
                if reach[v] < low[edge]:
                    edges.append(edge)

print(find_edges(graph))
print(get_edges(graph))



def partition(arr):
    if sum(arr) % 2 != 0:
        return False 
    
    target_sum = sum(arr)//2
    n = len(arr)

    return recursion_partition(arr,n,target_sum//2)


def recursion_partition(arr,n,target):
    if target == 0:
        return True 
    
    if n == 0 and target != 0:
        return False 
    
    if arr[n-1] > target:
        return recursion_partition(arr,n-1,target-arr[n])
    
    return recursion_partition(arr,n-1,target-arr[n-1]) or recursion_partition(arr,n-1,target)

arr = [61, 90, 85, 19, 20, 96, 75, 20, 28, 13, 93, 88, 8, 35, 59]
print(partition(arr))
