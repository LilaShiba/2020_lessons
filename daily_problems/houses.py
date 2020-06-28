'''
A robber has 2 options: 
a) rob current house i; 
b) don't rob current house.
If an option "a" is selected it means she can't rob previous i-1 house 
but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 
and all the following buildings.
So it boils down to calculating what is more profitable:
'''

def houses(arr, idx):
    if len(arr) < 1:
        return 0
    return max(rob(arr, idx+1), rob(arr, idx+2) + arr[idx])

def h(arr,idx,memo):
    if idx in memo:
        return memo[idx]
    if idx >= len(arr):
        return 0
   current = max(rob(arr,idx+1), rob(arr,idx+2) + arr[idx])
   memo[idx] = current
   return current

def rob(self, arr: List[int]) -> int:
    n = len(arr)
    if n <= 1:
        return arr[0]
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[1]

    for sp in range(2, n):
        val = arr[sp]
        dp[sp] = max(dp[sp-1], dp[sp-2] + val)
    return dp[n-1]