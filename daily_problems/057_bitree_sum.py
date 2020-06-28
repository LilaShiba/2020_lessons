'''
This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), 
return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).

'''
class Node:
    def __init__(self, value):
        self.v = value 
        self.r = None 
        self.l = None 
    def inverse(self):
        root = self
        queue = [root]

        while queue:
            node = queue.pop()
            if node:
                node.r, node.l = node.l, node.r 
                queue.append(node.l)
                queue.append(node.r)
        return root

    def inorder(self):
        root = self 
        if root.l:
            root.l.inorder()
        print(root.v)
        if root.r:
            root.r.inorder()
    
    def add(self, value):
        if value > self.v:
            if self.r:
                return self.r.add(value)
            self.r = Node(value)
        if value < self.v:
            if self.l:
               return self.l.add(value)
            self.l = Node(value)
    
    def print_level(self):
        stack = [self]
        while stack:
            node = stack.pop(0)
            if node.l != None:
                stack.append(node.l)
            if node.r != None:
                stack.append(node.r)
            print(node.v)

    def search_sum(self, ranges):
        node_min, node_max = ranges
        stack = [self]
        ans = 0

        while stack:
            node = stack.pop(0)
            if node_min <= node.v < node_max:
                #print(node.v)
                ans += node.v
            if node.l != None:
                stack.append(node.l)
            if node.r != None:
                stack.append(node.r)
        msg = f"The sum of nodes in range {node_min} to {node_max} is {ans}"
        print(msg)

if __name__ == "__main__":
    arr = [3,8,2,4,10,6]
    root = Node(5)
    for x in arr:
        root.add(x)
    root.inorder()
    root.search_sum([4,9])
    iroot = root.inverse()
    iroot.inorder()