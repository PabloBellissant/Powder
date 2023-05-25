
from Enum import *

class particle:
    def __init__(self, particleId, x, y, temperature):
        self.ID = particleId
        self.getX = x
        self.getY = y
        self.getTemperature = temperature
        self.getPressure = 1
        self.getConcentration = 0
        self.isBurning = False
# After
        self.nextX = self.getX
        self.nextY = self.getY
        self.nextTemperature = self.getTemperature
        self.nextPressure = self.getPressure
        self.nextConcentration = self.getConcentration
        self.nextIsBurning = self.isBurning

    def getFriends(self):
        checkList = [(-1,1),(0,1),(1,1),(0,-1),(1,0),(-1,-1),(-1,0),(1,-1)] # 8 positions to check

        friends = []

        x = self.getX
        y = self.getY

        for i in range(8):
            friend = particlesDictCoordinate.get((x + checkList[i][0], y + checkList[i][1]))
            if not friend == None:
                friends.append(friend)
        return friends

    def smoothTemp(self):
        friends = self.getFriends()

        multiply = (1.1-getHeatConductivity(self.ID))*50

        friendsTemp = 0
        for friendTemp in friends:
            friendsTemp += friendTemp.getTemperature
        friendsTemp /= (len(friends))
        return ((self.getTemperature*multiply) + friendsTemp )/ (1+(1*multiply))


    def getNewIdAtLowTemp(self):
        return getLowTempId(self.ID)

    def getNewIdAtHighTemp(self):
        return getHighTempId(self.ID)

    def getWichTempLowId(self):
        return getIdLowTemp(self.ID)

    def getWichTempHighId(self):
        return getIdHighTemp(self.ID)

    def getName(self):
        return getName(self.ID)

    def getColor(self):
        return getColor(self.ID)



particlesDictCoordinate = {}



for i in range(100):
    for p in range(50):
        particlesDictCoordinate[(i + 5, p + 5)]=(particle(1, i+5, p+5, 20))

particlesDictCoordinate.get((50,25)).getTemperature = 1500

particlesDictCoordinate.get((20,10)).getTemperature = -200

