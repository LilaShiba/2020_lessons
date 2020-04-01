# This problem was asked by Amazon.
# 
# Huffman coding is a method of encoding characters 
# based on their frequency. Each letter is assigned 
# a variable-length binary string, such as 0101 or 111110, 
# where shorter lengths correspond to more common letters. 
# To accomplish this, a binary tree is built such that the 
# path from the root to any leaf uniquely maps to a character. 
# When traversing the path, descending to a left child corresponds 
# to a 0 in the prefix, while descending right corresponds to 1.
# 
# Here is an example tree (note that only the leaf nodes have letters):
# 
#         *
#       /   \
#     *       *
#    / \     / \
#   *   a   t   *
#  /             \
# c               s
# 
# With this encoding, cats would be represented as 0000110111.

class Node:
    def __init__(self,v,name):
        self.v = v
        self.name = name
        self.r = None
        self.l = None

        
def trie(words):
    trie = {}
    for word in words:
        current = trie 
        for letter in word:
            current = current.setdefault(letter, {})
        current['#']='#'
    return trie

def sort_letters(word):
    ans = []
    for letter in word:
        if letter not in ans:
            ans.append((letter,word.count(letter)))
    return sorted(ans, key=lambda x:x[1], reverse=False)

def make_tree(word):
    height = len(word)
    print(height)
    
word = sort_letters('cat')
print(word)
print(make_tree(word))
            