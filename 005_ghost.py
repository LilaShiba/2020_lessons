# Ghost is a two-person word game where players alternate 
# appending letters to a word. The first person who spells 
# out a word, or creates a prefix for which there is no 
# possible continuation, loses. Here is a sample game:
# 
# Player 1: g
# Player 2: h
# Player 1: o
# Player 2: s
# Player 1: t [loses]
# 
# Given a dictionary of words, determine the letters the 
# first player should start with, such that with optimal 
# play they cannot lose.
# 
# For example, if the dictionary is ["cat", "calf", "dog", "bear"], 
# the only winning start letter would be b.

class Trie:
    def __init__(self, words=[]):
        self.trie = {}
        for word in words:
            self.add(word)
    
    def add(self, word):
        root = self.trie
        for letter in word:
            if letter in root:
                root = root[letter]
            else:
                root = root.setdefault(letter, {})
        root['#'] = '#'
        
    
    def get(self,prefix):
        root = self.trie
        for letter in prefix:
            if letter in root:
                root = root[letter]
            else:
                return None
        return root
        
    def show(self):
        print(self.trie)
        
    
def is_winning(trie, prefix):
    # returns letters that follow prefix
    root = trie.get(prefix)
    # if it's the end of the word
    if "#" in root:
        return False
    else:
        # returns next letters in trie
        next_letters = [prefix + letter for letter in root]
        # recursive call
        if any(is_winning(trie, move) for move in next_letters):
            return False
        else:
            return True
    
def best_start(words):
    trie = Trie(words)
    winners = []
    # returns starting level letters
    starts = trie.trie.keys()
    for letter in starts:
        if is_winning(trie, letter):
            winners.append(letter)
    return winners
            
print(best_start(['hello', 'hey', 'help', 'foxy']))        
# trie = Trie(['hello', 'hey', 'help'])
# trie.show()
# # print(trie.get('he'))
# # print(trie.trie.keys())
# trie.is_winning('he')