def trie(words):
    trie = {}
    for word in words:
        current_trie = trie 
        for letter in word:
            current_trie = current_trie.setdefault(letter, {})
        trie['#'] = '#'
    return trie 
    

words = ['hello', 'ellos', 'mellos']

print(trie(words))