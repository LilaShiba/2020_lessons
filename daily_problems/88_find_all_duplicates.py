# https://leetcode.com/submissions/detail/358185527/
class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                ans.append(abs(x))
            else:
                nums[abs(x)-1] = -1 * nums[abs(x)-1]
        return ans