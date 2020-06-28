# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        res = self.subsets(nums[1:])
        res += [subset + [nums[0]] for subset in res]
        return res