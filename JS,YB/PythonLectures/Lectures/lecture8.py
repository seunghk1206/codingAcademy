def range(a, b):
    L = []
    while a < b:
        L.append(a)
        a += 1
    return L

def ListN(N):
    return [each + 1 for each in range(0, N)]

print(range(0, 7))

run = True
a = 0
while run == True:
    a += 1
    if a == 10000:
        run = False
    print(a)