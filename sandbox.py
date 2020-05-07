import heapq

def prims(adj_list, start):
    queue = [start]
    s = []
    heapq.heapify(queue)

    for vertex in adj_list:
        while queue:
            # weight, u
            _, node = heapq.heappop(queue)
            s.append(node)
            best_node = None 
            best_node_weight = float('inf')
            for edge in adj_list[node]:
                if edge[0] not in s and edge[1] < best_node_weight:
                    best_node = edge[0]
                    best_node_weight = edge[1]
            if best_node != None:
                heapq.heappush(queue, (best_node_weight, best_node))
        if vertex not in s:
            heapq.heappush(queue, (0, vertex))
    return s


        
            


adj_list = { 
    'a':[('b', 8), ('c', 6), ('d', 5)],
    'b':[('a', 8), ('d', 4)],
    'c':[('a',6), ('d', 3)],
    'd':[('a',5), ('b',4), ('c',3)]
    }

adj_list2 = {
    'a':[('b',8), ('f',1), ('h', 6), ('e',5)],
    'b':[('a',8), ('c',4), ('f',2)],
    'c':[('b',4), ('f',2), ('g',7)],
    'g':[('c',7), ('f',9)],
    'f':[('g',9), ('c',2), ('b', 6), ('a',1), ('h',5)],
    'h':[('f',5), ('a',6), ('e',3)],
    'e':[('a',5), ('h',3)]
    }

# print(prims(adj_list, (0,'a')))


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
    reach = low = {v:float('inf') for v in graph}
    visited = {v:False for v in graph}
    depth = 0
    edges = []

    for v in graph:
        if not visited[v]:
            dfs(graph, v, v, reach, low, visited, depth, edges)
    return edges 

def dfs(graph,u,v, reach, low, visited, depth, edges):
    low[v] = reach[v] = depth 
    visited[v] = True 

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph,v,edge,reach,low,visited,depth+1, edges)
                low[v] = min(low[v], low[edge])
                if reach[v] < low[edge]:
                    edges.append(edge)

#print(get_edges(graph))






def bounce(runway, planeSpeed, planePos):
    # base case
    if planePos < 0 or planePos >= len(runway) or runway[planePos] == 1:
        return False 

    if planeSpeed == 0:
        print(planePos)
        return True
    
    for adjusted_speed in (planeSpeed+1, planeSpeed-1, planeSpeed):
        if bounce(runway, adjusted_speed, planePos+adjusted_speed):
            return True 
    return False
  
# print(bounce([0,0,1,0,0,0,0,0,0,0,0], 5, 0))

import random
price = [random.randint(0,50) for x in range(10)]
size = len(price)

def rod(price, size, memo):
    if size in memo:
        return memo[size]

    if size <= 0:
        return 0
    
    max_cut = 0
    for cut in range(size):
        max_cut = max(max_cut, price[cut] + rod(price, size-cut-1,memo))
    memo[size] = max_cut
    return max_cut


print(rod(price, size, {}))

def rood(price, size):
    table = [0 for _ in range(size+1)]

    for cut in range(1, size+1):
        max_cut = 0
        for current_cut in range(cut):
            max_cut = max(max_cut, price[current_cut] + table[cut-current_cut-1])
        table[cut] = max_cut
    return table[-1]

print(rood(price, size))
