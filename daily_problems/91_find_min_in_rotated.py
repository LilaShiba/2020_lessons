# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # if sorted
        if nums[0] < nums[-1]:
            return nums[0]
        
        # sliding window
        
        # for x in range(1, len(nums)-1):
        #     if nums[x-1] > nums[x]:
        #         return nums[x]
        #     elif nums[x+1] < nums[x]:
        #         return nums[x+1]
        # return nums[-1]
            
        
        l,r = 0, len(nums)-1
        
        while l < r:
            m = l + (r-l)//2
            # check for pivoit point
            # this problem is asking 
            # to find the pivoit
            if nums[m] > nums[m+1]:
                return nums[m+1]
            elif nums[m-1] > nums[m]:
                    return nums[m]
            # b-search
            else:
                if nums[r] > nums[m]:
                    r = m
                elif nums[r] < nums[m]:
                    l = m + 1
                else:
                    r = r - 1
        return nums[l]