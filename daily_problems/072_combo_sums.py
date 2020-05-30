# https://leetcode.com/problems/combination-sum-ii/

def comboFind(arr, target):
    ans = []
    arr = sorted(arr)

    def dp(target, current, idx):
        if target < 0:
            return
        if target == 0:
            ans.append(current)
        # dfs
        for x in range(idx, len(arr)):
            # if at the start or not a repeating number- because of sort on line 5
            if x == idx or arr[x-1] != arr[x]:
                dp(target-arr[x], current + [arr[x]], x+1)
    dp(target, [], 0)
    return ans

import collections
def bottomUp(candidates,target):
    dp = collections.defaultdict(set)
    candidates.sort()
    dp[0].add(())
    for n in candidates:
        for i in reversed(range(n, target + 1)):
            if i >= n:
                 for seq in dp[i-n]:
                    dp[i].add(seq+(n,))
    return dp[target]


def combosum(arr,target):
    ans = []
    arr.sort()

    def findsums(target,current,idx):
        if target == 0:
            ans.append(current) 
        if target < 0:
            return 

        for x in range(idx, len(arr)):
            if x == idx or arr[x] != arr[x-1]:
                findsums(target-arr[x], current + [arr[x]], x+1)
    findsums(target, [], 0)
    return ans
        


print(combosum([3,5,6,21,6,8,3,2,7], 8))

print(comboFind([3,5,6,21,6,8,3,2,7], 8))
# print(bottomUp([3,5,6,21,6,8,3,2,7], 8))

# print(bottomUp([2,1,3], 4))

#print(comboFind([2,1,3,2], 4))
