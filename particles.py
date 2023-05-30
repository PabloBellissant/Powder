import random


from Enum import *


ambiantHeat = 20

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

    def getSingleFriend(self, c1, c2):
        return particlesDictCoordinate.get((self.getX + c1, self.getY + c2))

    def smoothTemp(self):
        friends = self.getFriends()

        multiply = (1.01-getHeatConductivity(self.ID))*1000



        noneCount = friends.count(None)

        friendsTemp = 0
        for friendTemp in friends:
            if not friendTemp == None:
                friendsTemp += friendTemp.getTemperature

        count = len(friends) - noneCount
        if count != 0 :
            friendsTemp /= count
            multiply *= 1.5
            return ((friendsTemp * 5) + ambiantHeat + (self.getTemperature * multiply*3)) / (6 + multiply*3)
        else :
            return (ambiantHeat + (self.getTemperature*multiply*5)) / (1+multiply*5)




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

    def delete(self):
        if particlesDictCoordinate.get((self.getX, self.getY)) != None:
            particlesDictCoordinate.pop((self.getX, self.getY))

    def getDensity(self):
        return getDensity(self.ID)

    def getLiquidity(self):
        return getLiquidity(self.ID)




def create(x, y, id, temperature):
    if particlesDictCoordinate.get((x,y)) == None and particlesNextCoordinate.get((x,y)) == None:
        particlesDictCoordinate[(x, y)] = particle(id, x, y, temperature)
    if id == 0 : particlesDictCoordinate.get((x,y)).delete()



particlesDictCoordinate = {}
particlesNextCoordinate = {}
particlesNextCoordinate = particlesDictCoordinate










