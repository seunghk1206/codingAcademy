'''
a = [1,2,3,4,5,6,7,8,9,10,20,80]
print(a[0])
print(a[1])
b = 0
a[0]+ a[1] + a[2] ...
for each in a:
    b+=each
print(b)
'''
print(list(range(1, 10))) # a <= int < b
a = [1,2,3,4,5,6,7,8,9,10,20,80]
print(list(range(0, len(a)))) #0 <= int < len(a)
a = 0
for each in range(1, 8):
    if each%3 == 0:
        a += each
print(a)

1 ~ 20 숫자중에서 짝수끼리 더하는 함수를 만들어주세요.