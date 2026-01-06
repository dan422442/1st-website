from functools import cache
@cache
def f(n):
    if n==0:
        return 0
    return n*n-sum([f(n//i) for i in range(2,n+1)])
def g(n):
    return 3*(n*n-f(n)+n-1)
print(g(100000000))
