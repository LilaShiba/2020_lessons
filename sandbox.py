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

print(prims(adj_list, (0,'a')))


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
    reach = low = {v:float('inf') for v in graph}
    visited = {v: False for v in graph}
    depth = 0
    edges = []

    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, vertex, reach, low, visited, edges, depth)
    return edges

def dfs(graph,u,v,reach,low,visited,edges,depth):
    reach[v] = depth 
    low[v] = depth
    visited[v] = True 

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph, v, edge, reach, low, visited, edges, depth+1)
                low[v] = min(low[v], low[edge])
                if low[edge] > reach[v]:
                    edges.append(edge)

print(find_edges(graph))