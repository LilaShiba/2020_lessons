'''
This problem was asked by Quora.

You are given a list of (website, user) pairs that represent 
users visiting websites. Come up with a program that identifies 
the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
 
Then a reasonable similarity metric would most likely conclude that 
a and e are the most similar, so your program should return [('a', 'e')].


'''
arr = [('a', 1), ('a', 3), ('a', 5), 
    ('b', 2), ('b', 6), 
    ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
    ('d', 4), ('d', 5), ('d', 6), ('d', 7),
    ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
    
arr2 = [('a', 1), ('a',4), ('b',1), ('b',5), ('b',4), ('c',1), ('c',4 )]
 
def find_most_common(arr: tuple, k: int) -> list:
    arr = sorted(arr, key= lambda x:x)
    neighbors = {}
    for x,y in arr:
        if y not in neighbors:
            neighbors[y] = [x]
        else:
            neighbors[y].append(x)
    print(neighbors)
    l = list([x for x,y in neighbors.items()])
    return(l[:k])
    
        
#print(find_most_common(arr, 2))


'''
While there are several ways to mathematically represent similarity, 
one of the most straightforward is known as the Jaccard index, 
and is computed for two sets by 
dividing the size of their intersection by the size of their union.
'''

import collections

def jaccard_index(a,b, visitors):
    '''
    Intersection over Union
    The length of what is similar / the length of everything
    '''
    return len(visitors[a] & visitors[b]) / len(visitors[a] | visitors[b] )
    
def find_most_common(arr, k):
    visitors = collections.defaultdict(set)
    for site, user in arr:
        visitors[site].add(user)
    
    pairs = []
    sites = list(visitors.keys())
    
    for i in range(len(sites)-1):
        for j in range(i+1, len(sites)):
            score = jaccard_index(sites[i], sites[j], visitors)
            pairs.append((score, sites[i], sites[j]))
    return pairs

print(find_most_common(arr,1))
            
            