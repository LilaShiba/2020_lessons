import random, pprint, copy
     
def rotate_oranges(graph):
    fresh = {}
    rotten = {}
    n = len(graph)
    m = len(graph[0])
    mins = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                fresh[(i,j)] = 1
            elif graph[i][j] == 2:
                rotten[(i,j)] = 2
    
    while len(fresh) > 0:
        infected = []
        for x,y in rotten:
            for cx,cy in (x-1,y), (x,y-1), (x+1, y), (x, y+1):
                if 0<= cx < n and 0<= cy < m:
                    if graph[cx][cy] == 1:
                        fresh.pop((cx,cy), None)
                        infected.append((cx,cy))
                        graph[cx][cy] = 2
        
        if len(infected) == 0:
            return -1
        rotten = infected
        mins+=1

    return mins
matrix = [[random.randint(0,2) for _ in range(5)] for _ in range(5)]
graph = copy.deepcopy(matrix)
pprint.pprint(matrix)
print(rotate_oranges(graph))
pprint.pprint(matrix)    
    
    

        

