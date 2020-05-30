import random, pprint
matrix = [[random.randint(0,1) for _ in range(20)]for _ in range(10)]
pprint.pprint(matrix)

def numIslands(grid):
     # null case
    if not grid or len(grid) == 0:
        return 0
    # set up
    islands = 0
    n = len(grid)
    m = len(grid[0])
        
    def dfs(grid,x,y):
        # out of bounds
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
            
        grid[x][y] = 0
            
        dfs(grid, x+1, y)
        dfs(grid, x-1, y)
        dfs(grid, x, y+1)
        dfs(grid, x, y-1)
        return 1
        
        
    for x in range(n):
        for y in range(m):
            if grid[x][y] == 1:
                islands += dfs(grid, x, y)
    return islands
    

print(numIslands(matrix))
                        
                
        