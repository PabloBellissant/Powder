import random


from Enum import *


ambiantHeat = -10

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
            friends.append(friend)
        return friends

    def smoothTemp(self):
        friends = self.getFriends()

        multiply = (1.1-getHeatConductivity(self.ID))*50

        adder = 0
        friendsTemp = 0
        if friends.__contains__(None):

            adder = 1
            friendsTemp = ambiantHeat
        for friendTemp in friends:
            if not friendTemp == None:
                friendsTemp += friendTemp.getTemperature
        friendsTemp /= (len(friends)+adder)
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

    def isLiquid(self):
        return isLiquid(self.ID)

    def isSolid(self):
        return isSolid(self.ID)

    def isGaseous(self):
        return isGaseous(self.ID)

    def isPowder(self):
        return isPowder(self.ID)



particlesDictCoordinate = {}



for i in range(58):
    for p in range(33):
        particlesDictCoordinate[(i+20, p+10)]=(particle(1, i+20, p+10, 2))


particlesDictCoordinate.get((55,40)).getTemperature = 1000
particlesDictCoordinate.get((60,10)).getTemperature = 1000


