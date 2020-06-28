# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        
        while l < r:
            m = l+ (r-l)//2
            if target == nums[m]:
                return m
            if target >= nums[0] > nums[m]:
                r = m
            elif target < nums[0] < nums[m]:
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else: 
                r = m
        return -1
        