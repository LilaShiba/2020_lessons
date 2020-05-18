# https://leetcode.com/problems/minimum-cost-for-tickets/solution/

'''
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
'''

def minTicket(days, costs):
    n = days[-1]
    table = [float('inf') for _ in range(n+1)]
    table[0] = 0 

    for sp in range(1, n+1):
        table[sp] = table[sp-1]
        if sp in days:
            table[sp] =  min(
                table[sp-1] + costs[0],
                table[max(0, sp-7)] + costs[1],
                table[max(0, sp-30)] + costs[2] 
            )
    return table

def minTicket2(days, costs):
    n = days[-1]
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0

    for day in range(1, n+1):
        dp[day] = dp[day-1]
        if day in days:
            dp[day] = min(
                dp[day-1] + costs[0],
                dp[max(0,day-7)] + costs[1],
                dp[max(0,day-30)] + costs[2]
            )
    return dp


days = [1,4,6,7,8,20] 
costs = [2,7,15]
print(minTicket2(days,costs))
print(minTicket(days, costs))    
    
    

    