import random
arr = [random.randint(-10,10) for x in range(5)]

def kadens(arr):
    best = current = 0
    for int in arr:
        current = max(current+int, int)
        best = max(best, current)
    return current

print(arr)
print(kadens(arr))