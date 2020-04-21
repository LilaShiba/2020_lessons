import random
class Node:
    def __init__(self,v):
        self.v = v
        self.l = None
        self.r = None

    def inorder(self):
        stack = []
        current = self

        while True:
            if current:
                stack.append(current)
                current = current.l
            elif stack:
                current = stack.pop()
                print(current.v)
                current = current.r
            else:
                break

    def rorder(self):
        root = self
        if root.l:
            root.l.rorder()
        print(root.v)
        if root.r:
            root.r.rorder()

    def add(self, node):
        if node.v > self.v:
            if self.r:
                return self.r.add(node)
            self.r = node

        if node.v < self.v:
            if self.l:
                return self.l.add(node)
            self.l = node

        if node.v == self.v:
            return

    def rsearch(self, key):
        if self.v == None or self.v == key:
            print(self.v)
            return self.v

        if self.v < key:
            return self.r.search(key)
        if self.v > key:
            return self.l.search(key)

    def search(self,key):
        depth = 0
        current = self
        while True:
            if current.v == key or current == None:
                print('found', key, 'at depth', depth)
                return key

            if current.v > key:
                current = current.l
                depth += 1

            if current.v < key:
                current = current.r
                depth += 1





def inorder(root):
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.l
        elif stack:
            current = stack.pop()
            print(current.v)
            current = current.r
        else:
            break

arr = [random.randint(0,100) for x in range(10)]
arr[8] = 29
print(arr)

def make_tree(arr):
    root = Node(arr[0])
    for x in range(1, len(arr)):
        new_node = Node(arr[x])
        root.add(new_node)
    return root

root = make_tree(arr)
root.inorder()
root.search(29)
