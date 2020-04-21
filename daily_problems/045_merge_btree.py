class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

    def add(self,node):
        if self.v > node.v:
            if self.l:
                return self.l.add(node)
            self.l = node

        if self.v < node.v:
            if self.r:
                return self.r.add(node)
            self.r = node

        if self.v == node.v:
            print('duplicate', self.v)
            return

    def inorder(self):
        stack = []
        current = self
        return_stack = []

        while True:
            if current:
                stack.append(current)
                current = current.l
            elif stack:
                current = stack.pop()
                return_stack.append(current.v)
                current = current.r
            else:
                return return_stack
                break



def make_tree(arr):
    root = Node(arr[0])
    for x in range(1,len(arr)):
        new_node = Node(arr[x])
        root.add(new_node)
    return root

if __name__ == "__main__":
    import random
    a1 = [random.randint(0,100) for x in range(10)]
    a2 = [random.randint(0,100) for x in range(10)]
    root1 = make_tree(a1)
    root2 = make_tree(a2)

    r1 = root1.inorder()
    r2 = root2.inorder()
    r3 = r1 + r2
    print(r3)

    root = make_tree(r3)
    ans = root.inorder()
    print(ans)
