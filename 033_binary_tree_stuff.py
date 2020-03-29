class Node:
    def __init__(self,v):
        self.v = v
        self.l = None
        self.r = None

    def show_by_lvl(self,root):
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.l:
                stack.append(node.l)
            if node.r:
                stack.append(node.r)
            print(node.v)



def prune_tree(root):
    '''
    Given a
    binary tree, convert it to a full one by removing nodes
    with only one child.
    '''

    queue = [root]
    ans = []
    pans = []
    lvl = 0

    while queue:
        node = queue.pop(0)
        if node.l and node.r:
            queue.append(node.l)
            queue.append(node.r)
            ans.append(node)
            pans.append(node.v)
            lvl += 1
        elif node.l and not node.r:
            queue.append(node.l)
        elif node.r and not node.l:
            queue.append(node.r)
        if not node.l and not node.r:
            ans.append(node)
            pans.append(node.v)
    print(pans)
    return ans, lvl

def make_tree(arr):
    if len(arr) < 1:
        return
    mid = len(arr)//2
    node = arr[mid]
    node.l = make_tree(arr[:mid])
    node.r = make_tree(arr[mid+1:])
    return node


#          0
#       /     \
#     1         2
#   /            \
# 3                 4
#   \             /   \
#     5          6     7
# You should convert it to:
#      0
#   /     \
# 5         4
#         /   \
#       6     7


root = Node(0)
root.l = Node(1)
root.r = Node(2)

root.l.l = Node(3)
root.l.l.r = Node(5)
root.r.r = Node(4)
root.r.r.l = Node(6)
root.r.r.r = Node(7)
#show_by_lvl(root)
tree,lvl = prune_tree(root)
new_tree = make_tree(tree)
new_tree.show_by_lvl(new_tree)
