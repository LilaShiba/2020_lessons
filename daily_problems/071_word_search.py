# https://leetcode.com/problems/word-search/
from typing import List
import pprint

def wordSearch(board: List[List[str]], word: str) -> bool:
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0] and dfs(board, i, j, 0, word):
                return True 
    return False
                
    
def dfs(board, i, j, count, word):
    # end condition True
    if count == len(word):
        return True 
    # false conditions
    if 0 <= i < len(board) and 0<= j < len(board[0]) and board[i][j] == word[count]:
       
        temp = board[i][j]
        board[i][j] = ''

        found = dfs(board, i+1, j, count+1, word) or dfs(board, i-1, j, count+1, word) or dfs(board, i, j+1, count+1, word) or dfs(board, i, j-1, count+1, word)
        board[i][j] = temp 
        return found
    return False



def wordSearchDFS(board: List[List[str]], word: str) -> bool:
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0] and dfsS(board, i, j, 0, word):
                return True 
    return False

def dfsS(board,i,j,count,word):
    if count == len(word):
        return True
    
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[count]:
        temp, board[i][j] = board[i][j], ''
        found = dfsS(board, i+1, j, count+1, word) or dfsS(board, i-1, j, count+1, word) or dfsS(board,i,j+1, count+1, word) or dfsS(board,i, j-1, count+1, word)
        board[i][j] = temp 
        return found
    return False




board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]




w1 = "ABCCED"
w2 = "SEE"
w3 = "ABCB"
print(wordSearchDFS(board, w2))

  