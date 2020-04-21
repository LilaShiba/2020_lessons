class Node:
    def __init__(self,v):
        self.v = v
        self.r = None
        self.l = None

    def add(self, key):
        if self.v < key:
            if self.r:
                return self.r.add(key)
            self.r = Node(key)
        if self.v > key:
            if self.l:
                return self.l.add(key)
            self.l = Node(key)
        if self.v == key:
            return

    def inorder(self):
        root = self
        stack = []
        ans = []

        while True:
            if root != None:
                stack.append(root)
                root = root.l
            elif stack:
                root = stack.pop()
                ans.append(root.v)
                root = root.r
            else:
                break
        return ans


    def make_cart(self):
        print('inorder of make cart')
        arr = self.inorder()
        print(arr)
        arr = sorted(arr, key=lambda x:x)
        mid = len(arr)//2
        root = Node(arr[mid])
        print('root', root.v)
        for x in arr:
            root.add(x)
        return root


import random
arr = [random.randint(0,100) for x in range(10)]

def make_tree(arr):
    root = Node(arr[0])
    for x in range(1, len(arr)):
        new_node = arr[x]
        root.add(new_node)
    return root

root = make_tree(arr)
print('root in order')
root.inorder()
print('make new root')
new_root = root.make_cart()
print(new_root.inorder())
