#https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, val=0, left=None, right=None):
        # self.val = val
        # self.left = left
        # self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
    
        left_count, right_count = 0,0
        self.best = 0
        if root.right:
            right_count = self.zig(root.right, True) + 1
        if root.left:
            left_count = self.zig(root.left, False) + 1
        return max(self.best, right_count, left_count)
        
        
        
    def zig(self, root, direction):
        right_count, left_count = 0,0
        
        if root.right:
            right_count = self.zig(root.right, True) + 1
        if root.left:
            left_count = self.zig(root.left, False) + 1
        self.best = max(self.best, left_count, right_count)
        return left_count if direction else right_count
        
    