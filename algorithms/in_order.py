class Node:
    def __init__(self,v):
        self.v = v
        self.right = None
        self.left = None
        
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.v)
    in_order(node.right)


def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.v)
    if node.right:
        inorder(node.right)
        
        
root = Node(10)
root.left = Node(8)
root.right = Node(9)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

in_order(root)
inorder(root)