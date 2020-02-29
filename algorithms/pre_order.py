class Node:
    def __init__(self,v):
        self.v = v
        self.right = None
        self.left = None
    
    def pre_order(self):
        # (root,left,right)
        nodeStack = [self]
        
        while nodeStack:
            node = nodeStack.pop()
            print(node.v)
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)