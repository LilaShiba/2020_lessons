# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def getSum(root, current):
        
        
            if root.left != None and root.right != None:
                return getSum(root.left, current + str(root.val)) + getSum(root.right, current + str(root.val))

            elif root.left != None:
                return getSum(root.left, current + str(root.val))

            elif root.right != None:
                return getSum(root.right, current + str(root.val))
            else:
                return int(current+str(root.val))
        
        if not root:
            return 0
        return getSum(root, "0")
       