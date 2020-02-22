# http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/
import heapq

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
    print(heap)
    heapq.heapify(heap)
    return heap



        
def make_tree(heap):
    
    
    while len(heap) > 1:
        f1, n1 = heapq.heappop(heap)
        f2, n2 = heapq.heappop(heap)
        print(f2)
        node = Node('*', left=n1, right=n2)
        num = f1 + f2
        heapq.heappush(heap, (num, node))
    print(heap)
        


def compress(text_path, output):

    with open(text_path, "r") as file, open(output, "w") as fh:
        text = file.read()
        text = text.rstrip()
        frequency = letter_count(text)	    
    print(frequency)     
    

#compress('./dumbtxt.txt', 'wow.txt')
data = 'tacocats are super cool'
heap = letter_count(data)
make_tree(heap)