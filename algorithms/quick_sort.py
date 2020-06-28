# logic of quick sort
# this implementation defeats the strength of qs, which is memory allocation
# Great for interviews as it clearly shows logic
def qs(arr):
    if len(arr) > 1:
        pivot = arr[0]
        below = [x for x in arr if x < pivot]
        above = [x for x in arr if x > pivot]
        return qs(below) + [pivot] + qs(above)
    return arr


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

arr = [1,4,2,7,8,5,9]
print(qs(arr))
#print(quickSort(arr, 0, len(arr)-1))
