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
