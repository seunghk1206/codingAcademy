def sort(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L

def monetaryBuild(D2L):
    Sum = 0
    retL = []
    for each in D2L:
        if len(each)%10 == 0:
            for eachFact in each:
                Sum += eachFact
            retL.append(Sum/10)
            Sum = 0
    retL = sort(retL)
    return retL

def factorial(n):
    if n == 0:
        return 0
    else:
        return n * factorial(n-1)

print(monetaryBuild([[53, 42, 14, 32, 13, -13, -32, -4, -2, -3], 
 [35, 23, 53, 32, 42, 4, 35, -4, 10, 30],
 [63, 24, 33, 22, 28, 39, 29, 42, 28, 12],
 [2, 5, 32, 1]]))