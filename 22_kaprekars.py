'''
The number 6174 is known as Kaprekar's contant, 
after the mathematician who discovered an associated property: 
for all four-digit numbers with at least two distinct digits, 
repeatedly applying a simple procedure eventually results in 
this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the 
digits in x in ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174

Write a function that returns how many steps this will take for a given input N.

'''

def kaprekar_constant(num):
    count = 0
    t = list(str(num))
    if len(t) != 4:
        return False
    if len(set(t)) <= 1:
        return False

    
    
    while num != 6174:
        count += 1
        l_num = list(str(num))
        a = sorted(l_num, key=lambda x:x)
        d = sorted(l_num, key= lambda x:x, reverse=True)
        a,d = ''.join(a), ''.join(d)
        a,d = int(a),int(d)
        num = d-a
        print(num)
    print(count)
    return count
kaprekar_constant(3456)