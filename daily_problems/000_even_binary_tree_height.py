class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

def get_height(node):
    if not node:
        return 0
    
    l = get_height(node.l)
    r = get_height(node.r)
    return max(l, r) + 1
    
def is_even_height(root):
    rl = 0
    ll = 0
    stack = [root]
    
    while stack:
        node = stack.pop(0)
        if node.r:
            rl += 1
            stack.append(node.r)
        if node.l:
            ll += 1
            stack.append(node.l)
    return ll == rl, rl, ll
            

if __name__ == '__main__':
    root = Node(10)
    root.l = Node(5)
    root.r = Node(20)
    root.l.l = Node(15)
    root.l.r = Node(34)
    root.r.r = Node(44)
    root.r.l = Node(43)
    print(get_height(root))
    print(is_even_height(root))