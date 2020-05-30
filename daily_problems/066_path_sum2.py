# https://leetcode.com/problems/path-sum-ii/
'''
Given a binary tree and a sum, find all 
root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class Node:
    def __init__(self, v):
        self.v = v
        self.r = None 
        self.l = None

    def lvl_print(self):
        queue = [(self, 0)]

        while queue:
            node, lvl = queue.pop(0)
            print(f'{node.v}: {lvl}')
            if node.l != None:
                queue.append((node.l, lvl+1))
            if node.r != None:
                queue.append((node.r, lvl+1))
   
    #(root,left,right)
    def preorder(self):
        queue = [self]

        while queue:
            node = queue.pop()
            print(node.v)
            if node.r != None:
                queue.append(node.r)
            if node.l != None:
                queue.append(node.l)
    
    def get_paths(self,target):
        def find_paths(root, target, current, ans):
            if root == None:
                return 
                
            current.append(root.v)
            if root.v == target and root.l == None and root.r == None:
                ans.append(current)
                return
            
            find_paths(root.l, target-root.v, current.copy(), ans)
            find_paths(root.r, target-root.v, current.copy(), ans)
        ans = []
        find_paths(self, target, [], ans)  
        print(ans)
        return ans
    
    

if __name__ == "__main__":
    root = Node(5)
    root.l = Node(4)
    root.l.l = Node(11)
    root.l.l.l = Node(7)
    root.l.l.r = Node(2)
    root.r = Node(8)
    root.r.l = Node(13)
    root.r.r = Node(4)
    root.r.r.l = Node(5)
    root.r.r.r = Node(1)
    #root.lvl_print()
    #root.preorder()
    root.get_paths(22)