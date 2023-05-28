import random


from particles import particlesNextCoordinate



def gaseousNextPos(particle):



    p1 = particle.getSingleFriend(-1, -1)
    p2 = particle.getSingleFriend(0, -1)
    p3 = particle.getSingleFriend(1, -1)


    if p1 == None  or p2 == None  or p3 == None:
        x = particle.getX
        y = particle.getY - 1
        rdm = random.randint(-5, 5)
        if rdm < -4: x += -1
        elif rdm > 4: x += 1
        if particlesNextCoordinate.get((x,y)) == None :
            particle.nextX = x
            particle.nextY = y
            particlesNextCoordinate[(x,y)] = particle
    else :
        p4 = particle.getSingleFriend(-1, 0)
        p5 = particle.getSingleFriend(1, 0)

        if p4 == None or p5 == None:
            x = particle.getX
            y = particle.getY
            rdm = random.randint(-5, 5)
            if rdm < -1: x += -1
            elif rdm > 1: x += 1
            if particlesNextCoordinate.get((x,y)) == None :
                particle.nextX = x
                particle.nextY = y
                particlesNextCoordinate[(x, y)] = particle






