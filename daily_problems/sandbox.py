import random



# matrix = [[random.randint(0,1) for _ in range(200)]for _ in range(100)]


# def islands(grid):
#     islands = 0
#     n = len(grid)
#     m = len(grid[0])


#     def dfs(x,y):
#         if 0 <= x < n and 0<= y < m and grid[x][y]==1:
            
        
#             grid[x][y] = 0
#             dfs(x-1,y)
#             dfs(x,y-1)
#             dfs(x,y+1)
#             dfs(x+1, y)
#             return 1
#         return 0

#     for x in range(n):
#         for y in range(m):
#             if grid[x][y] == 1:
#                 islands += dfs(x,y)
#     return islands


# #print(islands(matrix))


# def bounces(runway, planeSpeed, planePos):
#     if planeSpeed == 0:
#         return True 
#     if planePos >= len(runway) or runway[planePos] == 1:
#         return False

#     return bounces(runway, planeSpeed-1, planePos+planeSpeed-1) or bounces(runway, planeSpeed+1, planePos+planeSpeed+1) or bounces(runway, planeSpeed, planePos+1)

# def r_bounce(runway, planeSpeed, planePos, memo):
#     # check memo
#     if planePos in memo and planeSpeed in memo[planePos]:
#         return memo[planePos][planeSpeed] != None

#     # add to memo
#     if planePos not in memo:
#         memo[planePos] = {}
    
#     # base case
#     if planeSpeed == 0:
#         return True 
#     # fail case
#     if planePos >= len(runway) or runway[planePos] == 1:
#         return False

#     # recursion 
#     for x in (planeSpeed-1), (planeSpeed+1), (planeSpeed):
#         if r_bounce(runway, x, planePos+x, memo):
#             memo[planePos][planeSpeed] = x
#             return True 
#     return False

# arr = [0,0,1,1,0,1,0,0,0,0,0]
# print(bounces(arr, 3, 0))
# print(r_bounce(arr, 3, 0, {}))

# import random
price = [random.randint(0,50) for x in range(10)]
size = len(price)

def rod(price,size):
    dp = [0 for _ in range(size+1)]
    price = [0] + price

    
    for cut in range(1, size+1):
        max_cut = 0
        for cost in range(1, len(price)):
            if cost <= cut:
                max_cut = max(max_cut, price[cost] + dp[cut-cost] )
        dp[cut] = max_cut
    return dp


# def memoCut(price,size,memo):
#     if size in memo:
#         return memo[size]
#     if size <= 0:
#         return 0
#     max_cut = 0
#     for cut in range(1,size+1):
#         max_cut = max(max_cut, price[cut] + memoCut(price, size-cut, memo))
#     memo[size] = max_cut
#     return max_cut

# def r_table(price,size):
#     table = [0 for x in range(size+1)]

#     for cut in range(1, size+1):
#         max_cut = 0 
#         for current_size in range(cut):
#             max_cut = max(max_cut, price[current_size] + table[cut-current_size-1])
#         table[cut] = max_cut
#     return table

# def rod(price, weight):
#     dp = [0 for _ in range(weight+1)]

#     for cut in range(1, weight+1):
#         for cost in range(cut):
#             dp[cut] = max(dp[cut], dp[cut-cost-1] + price[cost])
#     return dp 

# def howManyCombos(coins, coins_left, target):
#     if target == 0:
#         return 1
#     if target < 0:
#         return 0
#     if target > 0 and coins_left < 1:
#         return 0
#     return howManyCombos(coins, coins_left, target - coins[coins_left-1]) + howManyCombos(coins, coins_left-1, target)

# arr = [1,2,5]
# print(howManyCombos(arr, len(arr), 5))


# print(rod(price, size))
# print(r_table(price, size))
# print(rod(price, size))
# print(memoCut([0] + price, size, {}))

def canP(arr):
    if sum(arr) % 2 == 0:
        return partition(arr, sum(arr)//2, 0)
    return False 

def partition(arr, target, idx):
    if target == 0:
        return True 
    if idx >= len(arr) and target != 0:
        return False 
    if idx < 0:
        return False 
    
    return partition(arr, target-arr[idx], idx+1) or partition(arr, target, idx+1)

def find_partition(arr):
    total = sum(arr)
    if total % 2 == 0:
        return get_partition(arr, 0, 0, total, {})
    return False 

def get_partition(arr, idx, current_sum, total, memo):
    if (idx, current_sum) in memo:
        return memo[(idx,current_sum)]

    if current_sum * 2 == total:
        return True
    
    if idx >= len(arr) or total // 2 < current_sum:
        return False 
    
    memo[(idx, current_sum)] = get_partition(arr, idx+1, current_sum + arr[idx], total, memo) or get_partition(arr, idx+1, current_sum, total, memo)
    return memo[(idx, current_sum)]



def ppp(arr):
    total = sum(arr)
    if total % 2 == 0:
        return p(arr, total, 0, 0,{})
    return False


def p(arr, total, idx, current, memo):
    if (idx, current) in memo:
        return memo[(idx,current)]
    
    if current * 2 == total:
        return True 
    
    if idx >= len(arr) or total // 2 < current:
        return False 
    
    memo[(idx, current)] = p(arr, total, idx+1, current + arr[idx], memo) or p(arr, total, idx+1, current, memo)
    return memo[(idx, current)]



# arr = [random.randint(0,100) for _ in range(10)]
# print(canP(arr))
# print(find_partition(arr))
# print(ppp(arr))

def rrod(price, size, memo):
    if size in memo:
        return memo[size]
    
    if size <= 0:
        return 0

    max_cut = 0
    for cut in range(0, size):
        max_cut = max(max_cut, price[cut] + rrod(price, size-cut-1, memo))
    memo[size] = max_cut
    return max_cut



print(rrod(price,size, {}))
print(rod(price, size))

