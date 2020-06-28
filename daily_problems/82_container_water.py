# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        small = 0
        best_area = 0
        while left < right:
            # find restriction, which is smallest wall
            small = min(height[left], height[right])
            # find current area of water contained and compare to old max
            best_area = max(best_area, small * (right-left))
            # move pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best_area
        