"""
유저에게 input을 5번 받아서 그 input 을 제곱한 리스트로 리턴하는 
함수 "nSquare"를 작성해라
예제:
5
6
7
3
8

[25, 36, 49, 9, 64]
"""
'''
def nSquare():
    AnsL = []
    tempL = []
    for _ in range(5):
        inp = int(input())
        AnsL.append(inp)
    for each in AnsL:
        tempL.append(each**2)
    return tempL

print(nSquare())
'''
find = lambda x, y : x+y if x != 0 else 0
'''
def find(x,y):
    if x != 0:# not equal to
        return x+y
    else:
        return 0
'''

def nSquare():
    return [int(input())**2 for _ in range(5)]

print(find(1, 5))