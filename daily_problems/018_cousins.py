'''
This problem was asked by Yext.

Two nodes in a binary tree can be called cousins if 
they are on the same level of the tree but have different 
parents. For example, in the following diagram 4 and 6 
are cousins.

    1
   / \
  2   3
 / \   \
4   5   6

'''

class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None
        self.lvl = None
        self.parent = None
        

    def get_lvl(self) -> object:
        self.lvl = 0
        stack = [self]
        prev_node = self.v
        
        while stack:
            node  = stack.pop(0)
            current_lvl = node.lvl
            
            if node.r:
                node.r.parent = node.v
                node.r.lvl = current_lvl + 1
                stack.append(node.r)
            
            if node.l:
                node.l.parent = node.v
                node.l.lvl = current_lvl + 1
                stack.append(node.l)
                
    # left, root, right
    def inorder(self):
        root = self
        if root.l:
            root.l.inorder()
        print(root.v)
        if root.r:
            root.r.inorder()
    
    # root,left,right
    def pre_order(self):
        stack = [self]
        while stack:
            node = stack.pop()
            print(node.v)
            if node.r != None:
                stack.append(node.r)
            if node.l != None:
                stack.append(node.l)
    
    # level print 
    def level_print(self) -> int:
        stack = [self]
        while stack:
            node = stack.pop(0)
            if node.l != None:
                stack.append(node.l)
            if node.r != None:
                stack.append(node.r)
            print(node.v)
            
    def get_info(self) -> str:
        stack = [self]
        prev_node = self
        cousins = []
        
        while stack:
            node = stack.pop(0)
            if node.l != None:
                stack.append(node.l)
            if node.r != None:
                stack.append(node.r)
            
            print('node:',node.v, 'parent:', node.parent, 'level:', node.lvl )

    
    def get_cousins(self):
        self.lvl = 0
        stack = [self]
        lvl = {}
        lvls = []
        while stack:
            node = stack.pop(0)
            current_lvl = node.lvl
            lvl[(node.v, node.lvl)] = []
            lvls.append((node.lvl, node.parent, node.v))
            
            if node.r:
                node.r.lvl = current_lvl + 1
                node.r.parent = node.v
                lvl[(node.v, node.lvl)].append(node.r.v)
                stack.append(node.r)
            if node.l:
                node.l.lvl = current_lvl + 1
                node.l.parent = node.v
                lvl[(node.v, node.lvl)].append(node.l.v)
                stack.append(node.l)
        return lvl, lvls
            
            
    
def get_cousins(root,node,lvl):
    if lvl <= 1:
        return []
    cousins = []
    if lvl == 2:
        if root.l != node and root.r != node:
            if root.l:
                cousins.append(root.l.v)
            if root.r:
                cousins.append(root.r.v)
    else:
        cousins += get_cousins(root.l, node, lvl-1)
        cousins += get_cousins(root.r, node, lvl-1)
    
    return cousins       
    
        
        

root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)
root.r.r = Node(6)
#root.r.l = Node(7)
#cousins, lvls = root.get_cousins()
root.get_lvl()
root.get_info()


# c = []
# for node_lvl, node_parent, node_v in lvls:
#     for lvl, parent, value in lvls:
#         if node_lvl == lvl:
#             if node_parent != parent:
#                 c.append((node_v, value))
# print(c)

    
