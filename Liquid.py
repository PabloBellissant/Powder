import random

from particles import particlesDictCoordinate



def liquidNextPos(particle):

    particleFriend = particle.getFriends()
    if particleFriend[0] == None or particleFriend[1] == None or particleFriend[2] == None:
        x = particle.getX
        y = particle.getY + 1
        rdm = random.randint(-5, 5)
        if rdm < -4 : x += -1
        elif rdm > 4 : x += 1
        if particlesDictCoordinate.get((x,y)) == None :
            particle.nextX = x
            particle.nextY = y
    elif particleFriend[4] == None or particleFriend[6] == None:
        x = particle.getX
        y = particle.getY
        rdm = random.randint(-5, 5)
        if rdm < -1: x += -1
        elif rdm > 1: x += 1
        if particlesDictCoordinate.get((x,y)) == None :
            particle.nextX = x
            particle.nextY = y






