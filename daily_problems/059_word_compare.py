'''
This problem was asked by Google.

You are given a set of synonyms, such as (big, large) 
and (eat, consume). Using this set, determine if two 
sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
Note that the synonyms (a, b) and (a, c) do not necessarily 
imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that 
(a, b) and (a, c) do in fact imply (b, c)?
'''

def compare_words(s1,s2, synonyms):
    s1 = s1.split()
    s2 = s2.split()
    synonyms = {x:y for x,y in synonyms}

    for word in range(len(s1)):
        if s1[word] != s2[word]:
            if not synonyms[s1[word]] == s2[word]:
                return False
    return True



s1= "He wants to eat food."
s2="He wants to consume food."
s = [('big', 'large'), ('eat', 'consume')]
print(compare_words(s1,s2,s))