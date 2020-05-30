def dfs(node, adj_list, cache, target):
    if node not in cache:
        cache.append(node)
        if node == target:
            return True
        for edge in adj_list[node]:
            dfs(edge, adj_list, cache)
    return cache


import random
matrix = [[random.randint(0,10) for _ in range(5)]for _ in range(5)]

def mdfs(graph, x,y, visited):
    directions = ((1,0),(0,1),(-1,0),(0,-1))
    for edge in directions:
        cx = x + edge[0]
        cy = y + edge[1]
        if 0<= cx < len(graph) and 0<= cy <len(graph[0]):
            if (cx,cy) not in visited:
                visited[(cx,cy)] = (x,y)
                print(cx,cy)
                mdfs(graph,cx,cy,visited)
    return visited

parent = mdfs(matrix,0,0,{})

current = (4,4)
while current != (0,0):
    print(current)
    current = parent[current]


def bfs(graph, start, visited):
    queue = [start]
    visited[(0,0)] = 0
    
    while queue:
        x,y = queue.pop(0)
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        for edge in directions:
            cx = x + edge[0]
            cy = y + edge[1]
            if 0<= cx < len(graph) and 0<= cy <len(graph[0]):
                if (cx,cy) not in visited:
                    visited[(cx,cy)] = (x,y)
                    print(cx,cy)
                    queue.append((cx,cy))
    return parent

print(bfs(matrix, (0,0),{}))      
current = (4,4)
while current != (0,0):
    print(current)
    current = parent[current]