'''
This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)


'''


def smallest_squares(num):
    # base case
    if num <= 3:
        return num 
    res = num
    for x in range(1, num+1):
        temp = x*x 
        if temp > num:
            break
        res = min(res, 1+ smallest_squares(num-temp))
    return res 

print(smallest_squares(6))


# def numSquares(self, n: int) -> int:
# 	dp = [i for i in range(n+1)]
#     sqrs = [sq**2 for sq in range(1, int(n**0.5)+1)]
#     for i in range(1, n+1):
# 		dp[i] = min([dp[i-sq]+1 for sq in sqrs if i-sq>=0] + [dp[i]])
#     return dp[-1]


def bfs_squares(num):
    queue = [0]
    lvl = {0:0}
    paths = [x**2 for x in range(1,num+1) if x**2 <= num]
    path_len = len(paths)

    while queue:
        node = queue.pop(0)
        for x in range(path_len):
            if paths[path_len-x-1] <= num-node:
                sumPath = paths[path_len-x-1] + node
                if sumPath == num:
                    return lvl[node] + 1
                lvl[sumPath] = lvl[node] + 1
                queue.append(sumPath)


def bfs(num):
    queue = [(0,0)]
    visited = [True] + [False] * num 
    maxSq = int(num**.5)

    while queue:
        count, node = queue.pop(0)
        count+=1 
        for x in range(1, maxSq+1):
            temp = x**2 + node
            if temp <= num and not visited[temp]:
                if temp == num:
                    return count 
                visited[temp] = True 
                queue.append((count,temp))

print(bfs(6))
print(bfs_squares(6))