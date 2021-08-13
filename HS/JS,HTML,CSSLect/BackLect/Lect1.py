import sys
sys.setrecursionlimit(50000)
'''
print("hello world")
print(5/2)
print(5/2, end=' ')
print('shit')
a = str(5/2) + ' ' + 'shit'
print(a)

def eatMyAss(x):
    return x**3-5*x**2+3*x+5

print(eatMyAss(25000000))
'''
'''
a = True
i= 0
while a:
    print("eatMyAss")
    i += 1
    if i == 30000:
        a = False
'''
'''
a = [2,1,3,4,2,3,23,1,32,1,42,3,4,1,31,23,123]
for each in a:
    print(each)
    a.remove(1)
'''


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

# 9.22337*10^(18) 8byte로는 부족한 숫자.
def summation(x):
    if x == 0:
        return 0
    return x+summation(x-1)

print(summation(10))
def f(x):
    return x**12+6*x**11+7*x**10+6*x**4+3*x**3+2*x+3

def intFBody(b, accuracy, i):#100000000
    if accuracy == i:
        return (b/accuracy)*f(b/accuracy*i)
    return (b/accuracy)*f(b/accuracy*i)+intFBody(b, accuracy, i+1)

def intF(b, accuracy):#100000000
    return intFBody(b, accuracy, 0)

print(intF(12, 3220))

def intF(b):#100000000
    i=0
    limit = 3220
    deltaX = b/limit
    answer = 0
    while i <= limit:
        answer = answer + deltaX*f(deltaX*i)
        i = i+1
    return answer

print(intF(12))