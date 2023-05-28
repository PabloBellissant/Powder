import random


from particles import particlesNextCoordinate



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


    else :
        # Liquidity

        liquidity = int(particle.getLiquidity()*10)

        for i in range(liquidity):
            p4 = particle.getSingleFriend(-i, 0)
            p5 = particle.getSingleFriend(i, 0)

            if p4 == None or p5 == None:
                x = particle.getX
                y = particle.getY
                rdm = random.randint(1, 2)
                if rdm == 1: x -= i
                else : x += i
                if particlesNextCoordinate.get((x,y)) == None :
                    particle.nextX = x
                    particle.nextY = y
                    particlesNextCoordinate[(x, y)] = particle
                    break


