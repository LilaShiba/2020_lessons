# https://leetcode.com/problems/word-search/
class Solution:
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        def dfs(board,i,j,count,word):
            if count == len(word):
                return True 

            if 0 <= i < n and 0<= j < m and board[i][j] == word[count]:
                temp = board[i][j]
                board[i][j] = ""
                found = dfs(board, i+1, j, count+1, word) \
                    or dfs(board, i-1, j, count+1, word) \
                    or dfs(board, i, j+1, count+1, word) \
                    or dfs(board, i, j-1, count+1, word)
                board[i][j] = temp 
                return found 
            return False
    
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(board,i,j,0,word):
                    return True
        return False 
    
    