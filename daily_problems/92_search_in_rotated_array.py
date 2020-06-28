# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0, len(nums)-1
        
        while l <= r:
            m = l+ (r-l)//2
            if target >= nums[0] > nums[m]:
                r = m - 1
            elif target < nums[0] < nums[m]:
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else: 
                return m