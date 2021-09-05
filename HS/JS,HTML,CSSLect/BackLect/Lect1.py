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
def factorial(x):
    if x == 0:
        return 1
    return x*factorial(x-1)

print(factorial(2368))
#9.22337*10^(18) 8byte로는 부족한 숫자.
