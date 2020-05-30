# https://leetcode.com/problems/merge-two-sorted-lists/

def ms(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
    
        ms(left)
        ms(right)

        l=r=i = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[i] = left[l]
                l+=1
            else:
                arr[i] = right[r]
                r+=1
            i+=1
        
        while l < len(left):
            arr[i] = left[l]
            l+=1
            i+=1
        
        while r < len(right):
            arr[i] = right[r]
            r+=1
            i+=1
    return arr

arr1 = [11, 12, 14, 17, 22, 27, 28, 33, 57, 64]
arr2 = [6, 26, 32, 48, 66, 67, 81, 82, 88, 99]

def merge(l1, l2):
    ans = [0] * (len(l1) + len(l2))

    l = r = i = 0

    while r < len(l1) and l < len(l2):
        if l1[l] < l2[r]:
            ans[i] = l1[l]
            l+=1
        else:
            ans[i] = l2[r]
            r+=1
        i += 1
    while l < len(l1):
        ans[i] = l1[l]
        l+=1
        i+=1
    while r < len(l2):
        ans[i] = l2[r]
        r+=1
        i+=1
    return ans



    



if __name__ == '__main__':
    import random 
    arr1 = [random.randint(0,100) for _ in range(10)]
    arr2 = [random.randint(0,100) for _ in range(10)]
    l1 = ms(arr1)
    l2 = ms(arr2)
    print(merge(l1,l2))