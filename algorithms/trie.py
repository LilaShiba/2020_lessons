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


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        start = self.root
        
        for i in word:
            if i not in start:
                start[i] = {}
            start = start[i]
        start['$'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        start = self.root
        for i in word:
            if i not in start:
                return False
            start = start[i]
        return '$' in start
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start = self.root
        
        for i in prefix:
            if i not in start:
                return False
            start = start[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)