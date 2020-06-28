class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.right = right 
        self.left = left 
    
    def add(self, node):
        if node.val > self.val:
            if self.right != None:
                return self.right.add(node)
            self.right = node
        if node.val < self.val:
            if self.left != None:
                return self.left.add(node)
            self.left = node 

    def lvlPrint(self):
        queue = [self]
        arr = []
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            arr.append(node.val)

        print(arr)
    
    def pre_order(self):
        stack = [self]
        arr = []
        while stack:
            node = stack.pop()
            arr.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(arr)   

    def inorder(self, arr):
        root = self 
        if root.left:
            root.left.inorder(arr)
        arr.append(root.val)
        if root.right:
            root.right.inorder(arr)
        return arr   

    def invert(self):
        root = self
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                node.right, node.left = node.left, node.right 
                queue.append(node.right)
                queue.append(node.left)  
        return root




import random 
arr = [random.randint(0,100) for _ in range(10)]
root = Node(0)
for x in arr:
    n = Node(x)
    root.add(n)

root.lvlPrint()
root.pre_order()
print(root.inorder([]))
ir = root.invert()
print(ir.inorder([]))


