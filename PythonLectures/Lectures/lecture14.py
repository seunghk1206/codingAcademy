"""
import numpy as np
from PIL import Image as im


def main():
    tempL = []
    for _ in range(540):
        for _ in range(255+1):
            tempL.append(255)
    array = np.reshape(tempL, (540, 256))
    print(array)
    print(type(array))
    data = im.fromarray(array)
    data.save('gank.png')

if __name__ == "__main__":
    main()
"""

array1 = [0,4,5,6,2,4,6]
tempArr = []
for _ in range(255):
    tempArr.append(array1)
print(tempArr.index(array1))

class Human:
    def __init__(self, age, height, eyeColor, hairColor, weight):
        self.age = age
        self.height = height
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.weight = weight
[15, 170, 'brown', 'black', 56]
[Human(15, 170, 'brown', 'black', 56), Human(15, 170, 'brown', 'black', 56)]
"""
한 학년에 3개의 반이 있다. 그 반 안에서 각 사람의 정보를 담는 2d 리스트를 완성하여라.
사람의 정보는 클래스로 표현할수 있다. 각 반에 5명의 학생이 있다. 그 학생들의 정보는 알아서. 대신에 정보를 프린트도 해주어야 한다
"""
"""
for loop을 써서 n의 factorial을 리턴하는 함수, factorial을 작성하여라
"""