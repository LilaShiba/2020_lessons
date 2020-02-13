class Node:
    def __init__(self,v):
        self.v = v
        self.r = None
        self.l = None
        

    def zig_zag(self):
        ltr = True
        ans = [self]
        switch_arr = []
        lvl = 0
        
        while ans:
            node = ans.pop()
            print(node.v)
            if ltr:
                if node.l:
                    switch_arr.append(node.l)
                if node.r:
                    switch_arr.append(node.r)
            else:
                if node.r:
                    switch_arr.append(node.r)
                if node.l:
                    switch_arr.append(node.l)
            if len(ans) == 0:
                ltr = not ltr
                ans, switch_arr = switch_arr, ans


root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)
root.r.r = Node(7)
root.r.l = Node(6)
root.zig_zag()                
            
            
            