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
