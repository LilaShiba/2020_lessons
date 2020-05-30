'''
Given a value N, if we want to make change for N cents
 and we have infinite supply of each of S = { S1, S2, .. , Sm} 
 valued coins, how many ways can we make the change? The order 
 of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, 
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So the output should be 5.

'''
# how many ways
def coins_change(coins, coins_left, target):
    # base case target is met
    if target == 0:
        return 1
    # missed target :(
    if target < 0:
        return 0
    # if no solution
    if target > 0 and coins_left == 0:
        return 0
    # recurrance
    return coins_change(coins, coins_left-1, target) + coins_change(coins, coins_left, target-coins[coins_left-1])
    
# how many ways
def dp_coins(coins, target):
    # values from 0...target
    table = [0 for _ in range(target+1)]
    # if target is 0, there is 1 way to make change
    table[0] = 1

    for coin in range(len(coins)):
        for amount in range(coins[coin],target+1):
            table[amount] += table[amount-coins[coin]]
    return table

c = [1,3,5]
ways = len(c)
print(coins_change(c, len(c), 11))
# print(dp_coins(c, 5))


# least amount of coins to make amount x
# https://www.youtube.com/watch?v=1R0_7HqNaW0
def least_coins(coins, target):
    table = [target+1 for _ in range(target+1)]
    table[0] = 0

    # start with smallest subproblem and solve on up
    for i in range(target+1):
        # pick up all coins in subproblem
        for coin in range(len(coins)):
            cc = coins[coin]
            if cc <= i:
                table[i] = min(table[i], 1 + table[i-cc])
    return table


# bfs least coins
def bfs_least_coins(coins, target):
    queue = [0]
    next_queue = []
    how_many_coins = 0
    visited = [False] * (target+1)
    visited[0] = True
    while queue:
        how_many_coins += 1
        for edge in queue:
            for coin in coins:
                newVal = edge + coin
                if newVal == target:
                    return how_many_coins
                if newVal > target:
                    continue
                if not visited[newVal]:
                    visited[newVal] = True
                    next_queue.append(newVal)
        queue, next_queue = next_queue, []
    return False



coins = [1,2,5]
target = 11
# and = 3
# 5 + 5 + 1 = 11

def changeys(coins, target):
   # hold all subproblems
    dp = [target+1 for _ in range(target+1)]
    dp[0] = 0

     # all subproblems bottom up
    for sp in range(1, target+1):
       # all coins
        for coin in range(len(coins)):
            dp[sp] = min(dp[sp], dp[sp-coins[coin]] + 1)
    return dp

print(changeys(coins, target))
print(bfs_least_coins(coins, target))

def mm(coins,target):
    dp = [target+1 for _ in range(target+1)]
    dp[0] = 0

    for sp in range(1,target+1):
        for coin in coins:
            if coin <= sp:
                dp[sp] = min(dp[sp], 1+dp[sp-coin])
            else:
                break
    return dp

print(mm(coins,target))