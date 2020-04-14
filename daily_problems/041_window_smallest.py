'''
This problem was asked by Amazon.

Given a string, find the length of the smallest window that
contains every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
https://www.dailycodingproblem.com/solution/320?token=5b4a3e6e68e6e397faf0f602f0bc6d5a7b81da5f9c0b0bf436acb5e732acfc6d612aa915
'''

word = "jiujitsu"
ans = 5

def window(word):
    seen = []
    start = stop = 0
    start_letter = word[0]

    for idx, letter in enumerate(word):
        if letter not in seen:
            seen.append(letter)
        else:
            if letter == start_letter:
                start = start + 1
                start_letter = word[start]
        stop = idx

    return start, stop, word[start:stop+1]

print(window(word))
