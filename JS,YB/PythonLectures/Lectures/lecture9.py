def f(x):
    return x**2

def summation(x, limit):
    if x < limit:
        return f(x) + summation(x+1, limit)
    elif x == limit:
        return f(x)

def summationCube(limit):
    return limit*(limit+1)*(2*limit+1)/6

print(summation(3, 9))
print(summationCube(9) - summationCube(2))


tempL = [[1,2],[2,3]]
temp2L = [[3,4],[5,6]]
answer = []
'''
for i in range(len(tempL)):
    for j in range(len(tempL[i])):
        print(tempL[i][j])
'''
for j in range(len(tempL)):
    answer.append([])
    for i, each in enumerate(tempL[j]):
        answer[j].append(each + temp2L[j][i])
print(answer)

'''
i = 0
j = 0

while i<len(tempL):
    while j<len(tempL[i]):
        print(tempL[i][j])
        j += 1
    i += 1
'''

