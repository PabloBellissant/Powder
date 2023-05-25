# Inspiration : THE POWDER TOY


import pygame


from particles import *



ambientHeat = 22
pixelSize = 12


pygame.init()

screen = (1920, 1080)

win = pygame.display.set_mode(screen)

pygame.draw.rect(win, (255, 255, 255), pygame.Rect(70, 70, screen[0] - 140, screen[1] - 140), 2)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#DRAW
    for particle in list(particlesDictCoordinate.values()):
        x = particle.getX * pixelSize + 72
        y = particle.getY * pixelSize + 72
        pygame.draw.rect(win, particle.getColor(), pygame.Rect(x, y, pixelSize, pixelSize))

#CALCULATING
    #TEMPERATURE
    for particle in list(particlesDictCoordinate.values()):
        particle.nextTemperature = particle.smoothTemp()
        if particle.getTemperature > particle.getWichTempHighId():
            particle.ID = particle.getNewIdAtHighTemp()
        if particle.getTemperature < particle.getWichTempLowId():
            particle.ID = particle.getNewIdAtLowTemp()

        print(particle.getTemperature, particle.getName(), particle.ID)



#UPDATE ALL
    for particle in list(particlesDictCoordinate.values()):
        particle.getX = particle.nextX
        particle.getY = particle.nextY
        particle.getTemperature = particle.nextTemperature
        particle.getPressure = particle.nextPressure
        particle.getConcentration = particle.nextConcentration
        particle.isBurning = particle.nextIsBurning





    pygame.display.flip()


