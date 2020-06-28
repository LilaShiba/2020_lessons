import random
arr = [random.randint(0, 100) for x in range(25)]
arr = [-1,2,-8,-10]
def msort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        r = arr[mid:]
        l = arr[:mid]

        msort(r)
        msort(l)

        i=j=k = 0

        while i < len(r) and j < len(l):
            if r[i] < l[j]:
                arr[k] = r[i]
                i += 1
            else:
                arr[k] = l[j]
                j += 1
            k += 1

        while i < len(r):
            arr[k] = r[i]
            i += 1
            k += 1

        while j < len(l):
            arr[k] = l[j]
            j += 1
            k += 1
        return arr

print(msort(arr))
