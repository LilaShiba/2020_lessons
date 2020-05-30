# https://www.youtube.com/watch?v=1NXs_idViuQ
# https://leetcode.com/problems/reverse-vowels-of-a-string/

def reverse(word):
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
    arr = list(word)
    i,j = 0, len(word)-1
    
    while i < j:
        while i < j and arr[i] not in vowels:
            i += 1
        
        while i < j and arr[j] not in vowels:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1

    return ''.join(arr) 

print(reverse('hello'))
print(reverse('leetcode'))
print(reverse("Euston saw I was not Sue."))



