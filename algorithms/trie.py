def trie(words):
    trie = {}
    for word in words:
        current_trie = trie 
        for letter in word:
            current_trie = current_trie.setdefault(letter, {})
        trie['#'] = '#'
    return trie 

def in_trie(current_trie, word):
    for x in current_trie:
        if x not in current_trie:
            return False
        else:
            current_trie = current_trie[x]
    return True
    
def insert(trie, word):
    current_trie = trie
    for letter in word:
        if letter in current_trie:
            current_trie = current_trie[letter]
        else:
            current_trie[letter] = letter
    return trie
    

words = ['hello', 'ellos', 'mellos']

t = trie(words)
print(in_trie(t,'mellos'))
insert(t, 'hellos')
print(t)

class trieNode:
    def __init__(self,v):
        self.v = v
        self.children = None
        self.end = False


class Trie:
    def __init__(self):
        self.children = []
    
    def insert_word(self, word):
        for letter in word:
            if letter in self.children:
                self = self.find(letter)
            else:
                self.children.add_letter(letter)
    
    
    def find(self, letter):
        pass