class Human:
    def __init__(self, age, height, eyeColor, hairColor, weight):
        self.age = age
        self.height = height
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.weight = weight

classes = [[Human(15, 170, 'brown', 'black', 56) for each in range(5)] for each in range(3)]
def PrintInfo(classes, Class, attendanceNo, wantedInfo):
    if Class == 'A':
        ind = 0
    elif Class == 'B':
        ind = 1
    elif Class == 'C':
        ind = 2
    
    if wantedInfo == 'age':
        return classes[ind][attendanceNo-1].age
    elif wantedInfo == 'height':
        return classes[ind][attendanceNo-1].height
    