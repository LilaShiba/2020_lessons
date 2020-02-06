import random, heapq

matrix = [[random.randint(0,10) for x in range(10)] for y in range(10)]

def dijkstra(start, end, matrix, params=float('inf')):
    queue = []
    visited = {start:0}
    r = len(matrix)
    c = len(matrix[0])
    
    for row in range(r):
        for col in range(c):
            queue.append((float('inf'),row,col))
            visited[(row,col)] = float('inf')
    start = queue.pop(0)
    queue.insert(0, (0,0,0))
    heapq.heapify(queue)

    
    while queue:
        minNode = heapq.heappop(queue)
        current_weight, x,y = minNode
        
        
            
        neighbors = ((x+1, y), (x-1, y), (x, y-1), (x, y+1), (x-1,y-1), (x+1,y+1),(x-1,y+1),(x+1,y-1))
        real_neighbors = ((x,y) for x,y in neighbors if 0 <= x < r and 0 <= y < c and matrix[x][y] < params)
        
        for cx,cy in real_neighbors:
            cost = current_weight + matrix[cx][cy]
            if cost < matrix[cx][cy] + visited[(cx,cy)]:
                heapq.heappush(queue, (cost,cx,cy))
                visited[(cx,cy)] = cost
            if (cx,cy) == end:
                return visited[(cx,cy)]
    return visited
    
import random, heapq

matrix = [[random.randint(0,10) for x in range(10)] for y in range(10)]

def dijkstra_cleaned(start, end, matrix, params=float('inf')):
    queue = [start]
    heapq.heapify(queue)
    visited = {start:0}
    r = len(matrix)
    c = len(matrix[0])
    
    while queue:
        minNode = heapq.heappop(queue)
        weight,x,y = minNode

        
        if (x,y) == end:
            return visited[x,y]
            
        neighbors = ((x+1, y), (x-1, y), (x, y-1), (x, y+1), (x-1,y-1), (x+1,y+1),(x-1,y+1),(x+1,y-1))
        real_neighbors = ((x,y) for x,y in neighbors if 0 <= x < r and 0 <= y < c and matrix[x][y] < params)
        
        for cx,cy in real_neighbors:
            cost = weight + matrix[cx][cy]
            if (cx,cy) not in visited:
                
                heapq.heappush(queue, (cost,cx,cy))
                visited[(cx,cy)] = cost
    return False
    

print(dijkstra((0,0,0), (9,9), matrix))

print(dijkstra_cleaned((0,0,0), (9,9), matrix))
