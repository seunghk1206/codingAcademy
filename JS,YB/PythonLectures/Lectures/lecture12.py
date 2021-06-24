"""
def Quiz():
    Inp = str(input("The sky blue? True or False "))
    if Inp in ["True", "true", "T", "t"]:
        print("correct!")
    elif Inp in ["False", "false", "F", "f"]:
        print("incorrect!")
    else:
        print("invalid input")
Quiz()
"""
class Human:
    def __init__(self, age, height, eyeColor, hairColor, weight):
        self.age = age
        self.height = height
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.weight = weight
    def BMI(self):
        return self.weight/(self.height/100)**2

SHK = Human(25, 183, "brown", "black", 68)

print(SHK.BMI())

# n! = n*(n-1)!
# sigma(a, n, an) = sigma(a, n-1, an) + an(n)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)