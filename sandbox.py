# https://www.youtube.com/watch?v=3N47yKRDed0
def partition(arr, lenArr):
    current_sum = sum(arr)
    if current_sum % 2 == 0:
        return recursion(arr, lenArr, current_sum//2 )
    return False 
    

def recursion(arr, length, current_sum):
    if current_sum == 0:
        return True 
    if length == 0 and current_sum != 0:
        return False 
    if arr[length-1] > current_sum:
        return recursion(arr, length-1, current_sum)
    
    return recursion(arr, length-1, current_sum) or recursion(arr, length-1, current_sum-arr[length-1])


def nice_recursion(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    
    return canPartition(arr, 0, 0, total, {})

def canPartition(arr, idx, cur_sum ,total, memo):
    # memoization
    if (idx, cur_sum) in memo:
        return memo[(idx,cur_sum)]
    # base case
    if cur_sum * 2 == total:
        return True
    # False base case
    if cur_sum > total//2 or idx >= len(arr):
        return False
    
    memo[(idx,cur_sum)] = canPartition(arr, idx+1, cur_sum+ arr[idx], total, memo) or  canPartition(arr, idx+1, cur_sum, total, memo)
    return memo[(idx,cur_sum)]





def rr(arr):
    total = sum(arr)

    if total % 2 == 0:
        return can_pp(arr, 0, 0, total, {})
    return False 

def can_pp(arr, idx, cur_sum, total, memo):
    if (idx, cur_sum) in memo:
        return memo[(idx,cur_sum)]
    # True base case
    if cur_sum * 2 == total:
        return True 
    # False base case
    if idx >= len(arr) or cur_sum > total//2:
        return False 
    
    memo[(idx, cur_sum)] =  can_pp(arr, idx+1, cur_sum + arr[idx], total, memo) or can_pp(arr, idx+1, cur_sum, total, memo)
    return memo[(idx, cur_sum)]

import random
arr = [random.randint(0,100) for x in range(15)]
print(arr)
print(partition(arr, len(arr)))
print(nice_recursion(arr))
print(rr(arr))

coins = [1,2,5]
target = 11

def smallest_coins(coins, target):
    # hold all sub-problems
    table = [target+1 for _ in range(target+1)]
    # 0 coins = 0 change
    table[0] = 0

    # solve all subproblems bottom-up
    for subproblem in range(target+1):
        # simulate picking up all coins
        for coin in range(len(coins)):
            cc = coins[coin]
            if cc <= subproblem:
                table[subproblem] = min(table[subproblem], 1 + table[subproblem-cc])
    return table

def bfs_coin(coins, target):
    queue = [0]
    next_queue = []
    current_coin_count = 0
    vistited = [False for _ in range(target+1)]
    vistited[0] = True

    while queue:
        current_coin_count += 1
        for edge in queue:
            for coin in coins:
                next_coin = edge + coin  
                if next_coin == target:
                    return current_coin_count
                if next_coin > target:
                    continue
                if not vistited[next_coin]:
                    vistited[next_coin] = True 
                    next_queue.append(next_coin)
        queue, next_queue = next_queue, []
    return False

print(smallest_coins(coins, target))
print(bfs_coin(coins, target))

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
    visited = {x:False for x in graph}
    reach = low = {x:float('inf') for x in graph}
    edges = []
    depth = 0

    for vertex in graph:
        if not visited[vertex]:
            dfs(graph, vertex, vertex, visited, reach, low, edges, depth)
    return edges 


def dfs(graph, u, v, visited, reach, low, edges, depth):
    visited[v] = True 
    reach[v] = depth 
    low[v] = depth 

    for edge in graph[v]:
        if u != edge:
            if visited[edge]:
                low[v] = min(low[v], reach[edge])
            else:
                dfs(graph,v,edge,visited,reach,low,edges,depth+1)
                low[v] = min(low[v], low[edge])
                if low[edge] > reach[v]:
                    edges.append(edge)
    return edges
print(find_edges(graph))

def rod_cut(price,size, memo):
    if size in memo:
        return memo[size]
    if size <= 0:
        return 0

    max_cut = -float('inf')
    for cut in range(size):
        max_cut = max(max_cut, price[cut] + rod_cut(price, size-cut-1, memo))
    memo[size] = max_cut
    return max_cut
price = [random.randint(0,50) for x in range(10)]
size = len(price)

print(rod_cut(price,size,{}))


def recursion_rod(price, size, memo):
    if size in memo:
        return memo[size]
    if size <= 0:
        return 0
    max_cut = 0
    for cut in range(size):
        max_cut = max(max_cut, price[cut] + recursion_rod(price, size-cut-1, memo))
    memo[size] = max_cut
    return max_cut

def maxCut(price,size):
    dp = [0 for _ in range(size+1)]
    price = [0] + price 
    
    for cut in range(1, size+1):
        max_cut = 0
        for cost in range(1, len(price)):
            if cost <= cut:
                max_cut = max(max_cut, price[cost] + dp[cut-cost])
        dp[cut] = max_cut
    return dp
        

print(maxCut(price,size))
print(recursion_rod(price,size,{}))

days = [1,4,6,7,8,20]
costs = [2,7,15]
ans = 11


def minTicket(days, costs):
    n = days[-1]
    dp = [float('inf') for _ in range(n+1)]
    # no ticket/no days
    dp[0] = 0

    for day in range(1, n+1):
        dp[day] = dp[day-1]
        if day in days:
            dp[day] = min(
                dp[day-1] + costs[0],
                dp[max(0,day-7)] + costs[1],
                dp[max(0, day-30)] + costs[2]
            )
    return dp
print(minTicket(days, costs))

def combosum(arr, target):
    arr.sort()
    ans = []
    def findCombo(target,current,idx):
        if target == 0:
            ans.append(current)
        if target < 0:
            return 
        
        for x in range(idx, len(arr)):
            if x==idx or arr[x] != arr[x-1]:
                findCombo(target-arr[x], current + [arr[x]], x+1)
        
    findCombo(target,[],0)
    return ans
print(combosum([3,5,6,21,6,8,3,2,7], 8))