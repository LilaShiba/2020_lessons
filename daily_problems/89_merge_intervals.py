# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        merged = []
        
        for i in range(len(nums)):
            if merged == []:
                merged.append(nums[i])
            else:
                previous_end = merged[-1][1]
                current_start = nums[i][0]
                current_end = nums[i][1]
                if previous_end >= current_start:
                    merged[-1][1] = max(previous_end, current_end)
                else:
                    merged.append(nums[i])
        return merged