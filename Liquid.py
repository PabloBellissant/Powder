import random


from particles import particlesNextCoordinate
from particles import particlesDictCoordinate



def liquidNextPos(particle):




    x = particle.getX
    y = particle.getY + 1

    p2 = particle.getSingleFriend(0, 1)

    if not p2 == None :

        if random.randint(1,2) == 1:
            if particle.getSingleFriend(-1, 1) == None: x -= 1
            elif particle.getSingleFriend(1, 1) == None:x += 1
        else:
            if particle.getSingleFriend(1, 1) == None: x += 1
            elif particle.getSingleFriend(-1, 1) == None:x -= 1



    if particlesNextCoordinate.get((x,y)) == None :
        particle.nextX = x
        particle.nextY = y
        particlesNextCoordinate[(x,y)] = particle

    elif (p2.isLiquid() or p2.isGaseous() or p2.isPowder()) and p2.getDensity() < particle.getDensity():
            particle.ID, p2.ID = p2.ID, particle.ID
            particle.getPressure, p2.getPressure = p2.getPressure, particle.getPressure
            particle.getTemperature, p2.getTemperature = p2.getTemperature, particle.getTemperature
            particle.getConcentration, p2.getConcentration = p2.getConcentration, particle.getConcentration
            particle.isBurning, p2.isBurning = p2.isBurning, particle.isBurning


    else:
        # Liquidity

        x = particle.getX
        y = particle.getY

        liquidity = int(particle.getLiquidity() * 8)
        maxLeft = 0
        maxRight = 0
        # MAX LEFT
        for i in range(liquidity):
            if (particlesDictCoordinate.get((x-i - 1, y)) != None):
                break
        maxLeft = i + 1

        #MAX RIGHT
        for i in range(liquidity):
            if(particlesDictCoordinate.get((x+i+1, y)) != None):
                break
        maxRight = i + 1




        if maxLeft != 0 or maxRight != 0 :

            rdm = random.randint(-maxLeft+1, maxRight-1)

            x += rdm
            y+= random.randint(0,3)


        if particlesNextCoordinate.get((x, y)) == None:
            particle.nextY = y
            particle.nextX = x
            particlesNextCoordinate[(x, y)] = particle
