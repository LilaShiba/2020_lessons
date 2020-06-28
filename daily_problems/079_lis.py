# https://leetcode.com/problems/longest-increasing-subsequence/
import collections from defaultdict
# p algo
# O(nlogn)
def lis(nums):
    if not nums:
        return 0
    piles = [nums[0]]

    for n in range(1, len(nums)):
        placed = False
        for p in range(len(piles)):
            if nums[n] <= piles[p]:
                piles[p] = nums[n]
                found = True
                break
        if not found:
            piles.append(nums[n])
    return len(piles)

# dp
# O(N^2)
def lisDP(nums):
    if not nums:
        return 0 
    dp = [1] * len(nums)

    for sp in range(len(nums)):
        for cp in range(sp):
            if nums[sp] > nums[sp]:
                dp[sp] = max(dp[cp] +1, dp[nums])
    return max(dp)

# dp + b-search

def lengthOfLIS(self, nums: List[int]) -> int:
    tails = [0] * len(nums)
    ans = 0
        
    for num in nums:
        # b-search
        lo,hi = 0, ans
        while lo != hi:
            # no overflow
            m = lo + (hi-lo)//2
            if tails[m] < num:
                lo = m + 1
            else:
                hi = m
        tails[lo] = num
        ans = max(ans, lo+1)
    return ans

# O(2^N)
# Recursion

def bruteRecursionLIS(nums):
    def max_lis(idx, cur_max):
        if idx == len(nums):
            return 0
        if nums[idx] > cur_max:
            return max(1+max_lis(idx+1, nums[idx]), max_lis(idx+1, cur_max))
        
        return max_lis(idx+1, cur_max)
    return max_lis(0,0)

   