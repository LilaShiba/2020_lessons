# https://leetcode.com/problems/surrounded-regions/
from collections import defaultdict    
def solve(self, board: List[List[str]]) -> None:

    if not board or len(board) == 0:
        return []
        
    visited = defaultdict(set)
    n = len(board)
    m = len(board[0])
    # check perimeter for 0's. DFS and add to visted. These will not be flipped.
    top = [(0,x) for x in range(m) if board[0][x] == "O"]
    left = [(x,0) for x in range(n) if board[x][0] == "O"]
    bottom = [(n-1,x) for x in range(m) if board[n-1][x] == "O"] 
    right = [(x,m-1) for x in range(n) if board[x][m-1] == "O"]
        
    perimeter = top + bottom + left + right
        
    def dfs(x,y):
        if 0<= x < n and 0<= y < m and board[x][y] == 'O' and (x,y) not in visited:
            visited[(x,y)] = True
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            
        
    for x,y in perimeter:
        if (x,y) not in visited:
            dfs(x,y)
    print(visited)

    for x in range(n):
        for y in range(m):
            if board[x][y] == 'O' and (x,y) not in visited:
                board[x][y] = "X"

m = [["O","O","O"],["O","O","O"],["O","O","O"]]