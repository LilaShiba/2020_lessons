# This problem was asked by Yahoo.
# 
# Recall that a full binary tree is one in which each 
# node is either a leaf node, or has two children. Given a 
# binary tree, convert it to a full one by removing nodes 
# with only one child.
# 
# For example, given the following tree:
# 
#          0
#       /     \
#     1         2
#   /            \
# 3                 4
#   \             /   \
#     5          6     7
# You should convert it to:
# 
#      0
#   /     \
# 5         4
#         /   \
#       6     7


class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None
    
    def show(self):
        if self.l:
            self.l.show()
        print(self.v)
        if self.r:
            self.r.show()
            
        

def make_tree_binary(root, ans=[]):
        queue = [root]
        lvl = 0
        while queue:
            node = queue.pop(0)
            if node.l and node.r:
                lvl+=1
                ans.append(node.v)
                queue.append(node.l)
                queue.append(node.r)    
            if not node.l and not node.r:
                ans.append(node.v)

        return ans,lvl

def prune_tree(root):
    # if end
    if not root:
        return None
    
    # iterate
    prune_tree(root.l)
    prune_tree(root.r)
    
    # if binary or leaf
    if root.l and root.r or not root.l and not root.r:
        return root
    
    # Switch side to check
    if not root.l:
        root = root.r
    else:
        root = root.l
        
def get_lvl(node):
    if not node:
        return 0
    l = get_lvl(node.l)
    r = get_lvl(node.r)
    return max(l,r)+1


def convert(root):
    # if nothing
    if not root:
        return None
    # iterating
    root.l = convert(root.l)
    root.r = convert(root.r)
    
    # if leaf
    if not root.l and not root.r:
        return root

    if root.l and root.r:
        return root

    if not root.l:
        root = root.r
    else:
        root = root.l

root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.r.r = Node(4)
root.r.l = Node(5)
root.l.l = Node(6)
root.l.r = Node(7)

print(make_tree_binary(root))
print(get_lvl(root))
tree = prune_tree(root)
tree.show()

    
    