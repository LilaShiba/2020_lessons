import random

class Node:
    def __init__(self,v,r=None,l=None):
        self.v = v
        self.r = r
        self.l = l

    def add(self, node):
        if node.v > self.v:
            if self.r:
                root = self.r
                return root.add(node)
            else:
                self.r = node

        if node.v < self.v:
            if self.l:
                root = self.l
                return root.add(node)
            else:
                self.l = node

    def print_tree(self):
        if self.l:
            self.l.print_tree()
        print(self.v)
        if self.r:
            self.r.print_tree()

    def pre_order(self):
        #(root,left,right)
        nodeStack = [self]
        arr = []
        while nodeStack:
            node = nodeStack.pop()
            #print(node.v)
            arr.append(node.v)
            if node.r is not None:
                nodeStack.append(node.r)
            if node.l is not None:
                nodeStack.append(node.l)
        #print(arr)
        return arr

arr = [1,3,2,5,7,8,5,6,0]
arr2 = [random.randint(0,1000) for x in range(5)]

def bst_sort(arr):
    root = Node(arr[0])
    for x in range(1, len(arr)):
        new_node = Node(arr[x])
        root.add(new_node)
    return root

tree = bst_sort(arr)
tree.print_tree()
#tree.pre_order()
