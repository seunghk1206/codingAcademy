def factorial(x):
    if x == 0:
        return 1
    else: 
        return x * factorial(x-1)

def f(x, n):
    return (((-1)**n)*x**(2*n+1)/factorial(2*n+1))

def sin(x, n):
    if x%90 == 0:
        if (x//90)%2 == 1:
            if ((x//90)//2)%2 == 1:
                return -1
            else: 
                return 1
        else:
            return 0
    else:
        pi2deg = 3.1415/180
        if n == 0:
            return f(x*pi2deg, n)
        else:
            return f(x*pi2deg, n) + sin(x,n-1)

def g(x, n):
    return (((-1)**n)*x**(2*n)/factorial(2*n))

def cos(x, n):
    if x%90 == 0:
        if (x//90)%2 == 1:
            return 0
        else:
            if x%360 == 0:
                return 1
            else:
                return -1
    else:
        pi2deg = 3.1415/180
        if n == 0:
            return g(x*pi2deg, n)
        else:
            return g(x*pi2deg, n) + cos(x,n-1)

def tan(x, n):
    return sin(x, n)/cos(x, n)

print(sin(60, 84), cos(60, 84), tan(89, 84))