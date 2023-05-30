import random


from particles import particlesNextCoordinate



def powderextPos(particle):



    p1 = particle.getSingleFriend(-1, 1)
    p2 = particle.getSingleFriend(0, 1)
    p3 = particle.getSingleFriend(1, 1)


    if p1 == None  or p2 == None  or p3 == None:
        x = particle.getX
        y = particle.getY + 1
        rdm = random.randint(-5, 5)
        if rdm < -4: x += -1
        elif rdm > 4: x += 1
        if particlesNextCoordinate.get((x,y)) == None :
            particle.nextX = x
            particle.nextY = y
            particlesNextCoordinate[(x,y)] = particle

    elif (p2.isLiquid() or p2.isGaseous()) and p2.getDensity() < particle.getDensity():
        particle.ID, p2.ID = p2.ID, particle.ID
        particle.getPressure, p2.getPressure = p2.getPressure, particle.getPressure
        particle.getTemperature, p2.getTemperature = p2.getTemperature, particle.getTemperature
        particle.getConcentration, p2.getConcentration = p2.getConcentration, particle.getConcentration
        particle.isBurning, p2.isBurning = p2.isBurning, particle.isBurning
