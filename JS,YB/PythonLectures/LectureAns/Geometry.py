import random
import math

def volumeOfSphere(r):
    return 4/3*math.pi*r**3

def Geometry():
    lowerBound = float(input("Enter a smaller decimal number: "))
    upperBound = float(input("Enter a large decimal number: "))
    if upperBound < lowerBound:
        print("invalid input")
    else:
        r = random.uniform(lowerBound, upperBound)
        print("The volume of a sphere with radius, ", r, ", is: ", volumeOfSphere(r))

n = int(input("How many times do you want to run this program? "))
for _ in range(n):
    Geometry()