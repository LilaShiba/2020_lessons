from math import factorial

def pt(row):
    for n in range(row):
        for k in range(n+1):
            x = choose(n,k)
            print(x)


def combination(n, k):
    return int((factorial(n))/ (factorial(k) * factorial(n-k)))


def choose(n, k):
    if k in (0,n):
        return 1
    return choose(n-1, k-1) + choose(n-1, k)

def pascal(n):
    row = [1]
    k = [0]

    for x in range(n):
        row = [l+r for l,r in zip(row+k, k+row)]
    return row

print(pascal(3))


        
