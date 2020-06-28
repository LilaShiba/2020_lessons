class Node:
    def __init__(self,v):
        self.v = v
        self.r = None
        self.l = None 
        self.lvl = None
    
    def add(self, value):
        if value < self.v:
            if self.l:
                return self.l.add(value)
            self.l = Node(value)
        else:
            if self.r:
                return self.r.add(value)
            self.r = Node(value)
    
    def inverse(self):
        root = self 
        queue = [root]

        while queue:
            node = queue.pop()
            if node != None:
                node.l, node.r = node.r, node.l
        return root

    def preorder(self):
        root = self 
        queue = [root]
        ans = []

        while queue:
            node = queue.pop()
            #print(node.v)
            ans.append(node.v)
            if node.r != None:
                queue.append(node.r)
            if node.l != None:
                queue.append(node.l)
        print(ans)
    
    def pre_check(self):
        if self:
            print(self.v)
            if self.l != None:
                self.l.pre_check()
            if self.r != None:
                self.r.pre_check()
    
    def print_lvl(self):
        root = self 
        queue = [root]
        root.lvl = 0
        while queue:
            node = queue.pop(0)
            if node.l != None:
                node.l.lvl = node.lvl + 1
                queue.append(node.l)
            if node.r != None:
                node.r.lvl = node.lvl + 1
                queue.append(node.r)
            print(node.v, node.lvl)        

    def longest_path(self):
        '''
        find the longest consecutive path from parent to child. So, example below
        would return 2 as the path is 2-3, not 3-2-1.

               2
                \
                 3
                /
               2
             /
            1

        '''
        max_arr = [0]

        def find_path(root, count, target, max_arr):
            if root is None:
                return 
            elif root.v == target:
                count += 1
            else:
                count = 1
            
            max_arr[0] = max(max_arr[0], count)
            find_path(root.l, count, root.v + 1, max_arr)
            find_path(root.r, count, root.v + 1, max_arr)




        find_path(self, 0, 0, max_arr)
        print(max_arr)
        return max_arr[0]
        

arr = [2,3,4,5,6,7,8,9,10]
root = Node(1)
for x in arr:
    root.add(x)

# root.print_lvl()
# root.preorder()
root.longest_path()
