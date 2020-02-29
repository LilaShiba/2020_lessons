# http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

class Heapy():
    def __init__(self):
        self.heap = []
    
    def add(self, data):
        self.heap.append(data)
        self.heap = sorted(self.heap, key=lambda x:x[0])
        return self.heap
    
    def hpop(self):
        return self.heap.pop(0)
    
    def print_h(self):
        arr = []
        for x in self.heap:
            arr.append(x[0])
        print(arr)

class Node:
    
    def __init__(self, v, left=None, right=None):
        self.v = v 
        self.left = left
        self.right = right

def letter_count(data):
    frequency = dict()
    for letter in data:
        frequency[letter] = frequency.get(letter,0)+1
    heap = [(num, Node(letter)) for letter, num in frequency.items()]
    heap = sorted(heap, key=lambda x:x[0])
    #print(heap)
    return heap

        
def make_tree(data):
    heap = Heapy()
    for x in data:
        heap.add(x)

    while len(heap.heap) > 1:
        f1, n1 = heap.hpop()
        f2, n2 = heap.hpop()
        node = Node('*', left=n1, right=n2)
        num = f1 + f2
        heap.add((num, node))
        heap.print_h()

    return heap.heap[0][1]


        

def encode(root, string="", mapping={}):
    if not root:
        return

    if not root.left and not root.right:
        mapping[root.v] = string

    encode(root.left, string + "0", mapping)
    encode(root.right, string + "1", mapping)

    return mapping

def codes(root, string="", mapping={}):
    if not root:
        return
        
    if not root.left and not root.right:
        mapping[root.v] = string 
        
    codes(root.left, string + "0", mapping)
    codes(root.right, string + "1", mapping)
    return mapping

# def compress(text_path, output):
# 
#     with open(text_path, "r") as file, open(output, "w") as fh:
#         text = file.read()
#         text = text.rstrip()
#         frequency = letter_count(text)	    
#     print(frequency)     
# 

#compress('./dumbtxt.txt', 'wow.txt')
data = 'aaaa bb c'
heap = letter_count(data)
h = make_tree(heap)
print(h)
encoded = codes(h)
print(encoded)