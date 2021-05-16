def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
# 1 ~ n


#1 1 2 3 5 8 ...
print(fibonacci(6))