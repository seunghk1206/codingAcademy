import sys

sys.setrecursionlimit(10**9)

def summation(n):
    if n == 1:
        return 1
    return n+summation(n-1)
print(summation(20))