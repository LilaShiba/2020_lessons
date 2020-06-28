# create adj_list
# topographically sort
# backtrack -> use connected X list to max out o's using safe bfs grabbing o's while traversing x's
# 3 groups need 3 O's 2 x's

# Given a 5 x 5 region populated by 25 citizens, your task is to write a function that divides the region into 5 districts given the following conditions:
# 
# 10 citizens will vote for your candidate, while the other 15 will vote for the opponent
# Your candidate must win the popular vote for 3 of the 5 districts
# Each district must have an equal number of voters
# Each district must be one contiguous cluster of voters (i.e. each voter has one or more orthogonally adjacent neighbors from the same district)

import pprint
example_tests = [
	[
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX'],
	[
		'XOXOX',
		'OXXOX',
		'XXOXX',
		'XOXOX',
		'OOXOX'],
	[
		'OXOOX',
		'XXOXO',
		'XOXXX',
		'XXOXX',
		'OXXOO'],
	[
		'XXOXO',
		'XOXOX',
		'OXOXO',
		'XOXOX',
		'XXOXX'],# null
	[
		'XXXXX',
		'OOOXO',
		'XXXOX',
		'OOOOO',
		'XXXXX']
] 


def make_adj_list(matrix, type):
    adj_list = {}
    row = len(matrix)
    col = len(matrix[0])
    
    def get_neighbors(r ,c):
        
        neighbors = ((r+1, c), (r-1, c), (r, c-1), (r, c+1))
        real_neighbors = [(x,y) for x,y in neighbors if 0 <= x < row and 0<= y < col and matrix[x][y]==type]
        return real_neighbors
    
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == type:
                adj_list[(r,c)] = get_neighbors(r, c)
    return adj_list
    
def topo_sort(adj_list):
    visited = []
    for vertice in adj_list:
        dfs(adj_list, visited, vertice)
    return visited
    
def dfs(adj_list, visited, node):
    if node not in visited:
        visited.insert(0, node)
        for edge in adj_list[node]:
            dfs(adj_list, visited, node)

def bfs(matrix, x_list, visited=[]):
    r = len(matrix)
    c = len(matrix[0])
    ans = []
    x_count, o_count = 0,0
    
    while x_list:
        node = x_list.pop(0)
        x,y = node
        neighbors = ((x-1,y), (x+1,y), (x,y-1), (x,y+1))
        o_neighbors = [(x,y) for x,y in neighbors if 0<= x < r and 0<= y < c and matrix[x][y] == 'O']
        
            
        
# matrix = example_tests[1]
# pprint.pprint(matrix)

# adj_list = make_adj_list(matrix,'X')
# adj_listO = make_adj_list(matrix,'O')

# connections = topo_sort(adj_list)
# connectionsO = topo_sort(adj_listO)

# print(connections)
# print('o',connectionsO)


def can_win(matrix):
	