'''
This problem was asked by Etsy.

Given a sorted array, convert it into a height-balanced binary search tree.
'''

class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None
    def print(self):
        if self.l:
            self.l.print()
            print(self.l.v)
        if self.r:
            self.r.print()
            print(self.r.v)
    def lp(self):
        stack = [self]
        while stack:
            node = stack.pop(0)
            if node.l:
                stack.append(node.l)
            if node.r:
                stack.append(node.r)
            print(node.v)

    def level_print(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node.r:
                queue.append(node.r)
            if node.l:
                queue.append(node.l)
            print(node.v)


def make_tree(arr):
    # end condition
    if not arr:
        return
    # get change point
    mid = len(arr)//2
    # make tree
    root = Node(arr[mid])
    root.l = make_tree(arr[:mid])
    root.r = make_tree(arr[mid+1:])
    return root


arr = [1,2,3,4,5,6,7,8,9]
root = make_tree(arr)
root.lp()
root.level_print()
