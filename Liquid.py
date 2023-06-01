import random


from particles import particlesNextCoordinate
from particles import particlesDictCoordinate



def liquidNextPos(particle):




    x = particle.getX
    y = particle.getY

    p2 = particlesNextCoordinate.get((x, y+1))


    if p2 != None:


        if particle.liquidDirection: # If Left
            if particlesDictCoordinate.get((x-1, y)) == None: x -= round(random.random()+0.25)
            else : particle.liquidDirection = False
        else:
            if particlesDictCoordinate.get((x+1, y)) == None: x += round(random.random()+0.25)
            else : particle.liquidDirection = True


        if (p2.isLiquid() or p2.isGaseous() or p2.isPowder()) and p2.getDensity() < particle.getDensity():
            particle.ID, p2.ID = p2.ID, particle.ID
            particle.getPressure, p2.getPressure = p2.getPressure, particle.getPressure
            particle.getTemperature, p2.getTemperature = p2.getTemperature, particle.getTemperature
            particle.getConcentration, p2.getConcentration = p2.getConcentration, particle.getConcentration
            particle.isBurning, p2.isBurning = p2.isBurning, particle.isBurning



        if particlesNextCoordinate.get((x, y)) == None:
            particle.nextY = y
            particle.nextX = x
            particlesNextCoordinate[(x, y)] = particle




    elif particlesDictCoordinate.get((x, y+1)) == None:

        particle.nextX = x
        particle.nextY = y+1
        particlesNextCoordinate[(x,y+1)] = particle

