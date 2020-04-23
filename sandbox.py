s = 'babad'

def longest_pal(s):
    longest = ''
    for x in range(len(s)):
        for y in range(len(s)):
            print(s[x:y+1])

print(longest_pal('abbb'))

def lp(s):
    def is_pal(s):
        return s == s[::-1]
    longest = ''
    length = len(s)
    if is_pal(s):
        return s
    for x in range(length-1):
        for y in range(1, length):
            substring = s[x:y+1]
            if is_pal(substring) and len(substring) > len(longest):
                longest = substring
    return longest, 'woof'

print(lp('abbb'))


# def is_palindrom(sub):
#   return sub[::-1] == sub
#
# def palindrom(word):
#   longest = ''
#   length = len(word)
#   for x in range(length-1):
#     for y in range(1, length):
#       substring = word[x:y]
#       if is_palindrom(substring) and len(substring) > len(longest):
#         longest = substring
#   return longest
#
# print(palindrom(s))
