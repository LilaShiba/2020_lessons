#https://leetcode.com/problems/largest-divisible-subset/
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    n = len(nums)
    # because  in order for a % b == 0 a >= b
    nums.sort()
    dp = [[x] for x in nums]
        
    # for each subproblem
    for sp in range(len(nums)):
        # for each occurance in subproblem where sp >= j
        for j in range(sp):
            # if  a % b == 0 and longest subsequence (add nums divisable by j that have already been checked)
            if nums[sp] % nums[j] == 0 and len(dp[sp]) < len(dp[j])+1:
                dp[sp] = dp[j] + [nums[sp]]
    print(dp)
    return max(dp, key=len)