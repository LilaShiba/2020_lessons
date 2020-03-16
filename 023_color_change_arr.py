'''
This problem was asked by Facebook.

On a mysterious island there are creatures 
known as Quxes which come in three colors: 
red, green, and blue. One power of the Qux 
is that if two of them are standing next to 
each other, they can transform into a single 
creature of the third color.

Given N Quxes standing in a line, determine 
the smallest number of them remaining after 
any possible sequence of such transformations

For example, given the input 

['R', 'G', 'B', 'G', 'B'] 

it is possible to end up with a single Qux through the 
following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |


'''
arr = ['R', 'G', 'B', 'G', 'B'] 

def get_color(arr):
    '''
    Returns color of quxes
    '''
    if 'R' in arr and 'B' in arr:
        return 'G'
    elif 'R' in arr and 'G' in arr:
        return 'B'
    else:
        return 'R'
        
def make_small(arr):
    count = 0
    while count < len(arr)-1:
        a = arr[count]
        b = arr[count+1]
        if a != b:
            a = arr.pop(count)
            b = arr.pop(count)
            c = get_color([a,b])
            arr.insert(count,c)
            count = 0
        else:
            count += 1
    return arr

print(make_small(arr))
        