'''
The "look and say" sequence is defined as follows: beginning with the term 1, 
each subsequent term visually describes the digits appearing in the previous term. 
The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.

'''

def sequence(n:int) -> int:
    if n == '1':
        return '1'
    ans = '11'
    # loop bu counting down to base case of 11 aka 2
    while n != 2:
        # count is 1 because it is the default start
        count = 1
        # temp storage of instance ans
        temp = []
        for y in range(len(ans)):
            # if at the end add the ans
            if y+1 == len(ans):
                temp.append(str(count) + ans[y])
            # if elements are the same increment count
            elif ans[y] == ans[y+1]:
                count += 1
            # if a new element is next add old count and int to ans
            else:
                temp.append(str(count) + ans[y])
                count = 1
        # reset count
        count = 0
        # decrement loop
        n -= 1
        # update answer
        ans = ''.join(temp) 
        # init temp
        temp = ''    
    # return that beauitful answer
    return ans

print(sequence(4))




def count_and_say(num):
    if num == 1:
        return "1"
    string = '11'
    cnt = 0
    while num != 2:
        new_string = []
        cnt += 1
        for i in range(len(string)):
            if i+1 == len(string):
                new_string.append(str(cnt)+string[i])
            elif string[i] == string[i+1]:
                cnt += 1
            else:
                new_string.append(str(cnt)+string[i])
                cnt = 1
        cnt = 0
        num -= 1
        string = ''.join(new_string)
    return string    

#print(count_and_say(5))