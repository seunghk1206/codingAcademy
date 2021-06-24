def getPeriod(momentOfInertia, d, mass):
    return 2*3.1415*(momentOfInertia/(d*mass*10))**(1/2)

def getTerminalVelocity(m, b):
    return m*10/b