# https://www.youtube.com/watch?v=BfUejqd07yo
def kp(m, word, nums):
    p = 2**63 - 1 # to serve as mod to stop overflow
    current_hash_value = 0
    for l in range(mid):
        current_hash_value = (current_hash_value * 26 + nums[i]) % p 
    hashes = {current_hash_value}

    idx = -1
    max_pow = pow(26,mid,p)

    for i in range(mid, len(word)):
        # take out last value
        # add newest value
        # this slides the hash
        current_hash_value = (26*current_hash_value - nums[i-mid] * max_pow + nums[i]]) %p
        if current_hash_value in hashes:
            idx = i+1-mid
        hashes.add(current_hash_value)
    return idx



def rabin_karp(word, pattern):
    '''
        use a rolling hash to find a pattern
        in the string. We store letter ASCII 
        codes in a hash and then compare as
        we roll through the word
    '''
    n = len(word)
    m = len(pattern)    
    pv = sum([ord(pattern[x]) for x in range(m)])
    window = sum([ord(word[x]) for x in range(m)])
    ans = []
    last = 0
    for x in range(m, n):
        window-=ord(word[last])
        window+=ord(word[x])
        last +=1
        if window == pv:
            idx = (x-(m-1))
            if word[idx:idx+m] == pattern:
                ans.append(idx)
    return ans





print(rabin_karp('banana', 'ana'))