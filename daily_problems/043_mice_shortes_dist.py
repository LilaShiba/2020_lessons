'''
This problem was asked by Amazon.

Consider the following scenario: there are N mice and N holes placed at integer points
along a line. Given this, find a method that maps mice to holes such that the
largest number of steps any mouse takes is minimized.

Each move consists of moving one mouse one unit to the left or right,
and only one mouse can fit inside each hole.

For example, suppose the mice are positioned at [1, 4, 9, 15], and
the holes are located at [10, -5, 0, 16]. In this case, the best
pairing would require us to send the mouse at 1 to the hole at -5,
so our function should return 6.
'''

mice = [1, 4, 9, 15]
holes = [10, -5, 0, 16]

def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        right = arr[mid:]
        left = arr[:mid]

        merge_sort(right)
        merge_sort(left)

        r=l=k= 0

        while r < len(right) and l < len(left):
            if right[r] < left[l]:
                arr[k] = right[r]
                r += 1
            else:
                arr[k] = left[l]
                l += 1
            k += 1

        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1

        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1
        return arr


def smallest_moves(mice, holes):
    m = merge_sort(mice)
    h = merge_sort(holes)
    min_moves = 0
    best_pair = -float('inf')

    for idx, mouse in enumerate(mice):
        min_moves = mouse - h[idx]
        best_pair = max(min_moves, best_pair)


    return best_pair

print(smallest_moves(mice, holes))
