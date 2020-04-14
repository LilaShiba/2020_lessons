def fib_bottom_up(n):
    m = {}
    m[0] = 0
    m[1] = 1

    for x in range(2,n+1):
        m[x] = m[x-1] + m[x-2]
    return m[n]

def fib(n):
    a,b = 0,1
    for x in range(n):
        a,b = a+b, a
    return a

print(fib(6))

def naive_fib(n):
    if n <= 2:
        f = 1
    else:
        f = naive_fib(n-1) + naive_fib(n-2)
    return f

print(naive_fib(6))

def memo_fib(n, cache):
    # memo
    if n in cache:
        return cache[n]
    # base
    if n <= 2:
        return 1
    # subproblem
    cache[n] = memo_fib(n-1, cache) + memo_fib(n-2, cache)
    return cache[n]

print(memo_fib(6,{}))

def fibby(n):
    fib = {}
    for k in range(1,n+1):
        if k <= 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]

print(fibby(6))
