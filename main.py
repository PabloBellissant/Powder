# Inspiration : THE POWDER TOY
import time

import pygame


from particles import *
from Liquid import *



pixelSize = 12


pygame.init()
SCREEN_HEIGHT = pygame.display.Info().current_h  # 480
SCREEN_WIDTH = pygame.display.Info().current_w  # 480 × 2

screen = (SCREEN_WIDTH, SCREEN_HEIGHT)

win = pygame.display.set_mode(screen)




run = True
tBase = time.time()
fpsValue = 0
while run:
    t0 = time.time()
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(70, 70, screen[0] - 140, screen[1] - 140), 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#DRAW
    for particle in list(particlesDictCoordinate.values()):
        x = particle.getX * pixelSize + 72
        y = particle.getY * pixelSize + 72
        pygame.draw.rect(win, particle.getColor(), pygame.Rect(x, y, pixelSize, pixelSize))





#CALCULATING

    for particle in list(particlesDictCoordinate.values()):
        # TEMPERATURE

        particle.nextTemperature = particle.smoothTemp()
        if particle.getTemperature > particle.getWichTempHighId():
            particle.ID = particle.getNewIdAtHighTemp()
        if particle.getTemperature < particle.getWichTempLowId():
            particle.ID = particle.getNewIdAtLowTemp()


        # Gravity
        if particle.isLiquid():
            liquidNextPos(particle)








#UPDATE ALL
    for particle in list(particlesDictCoordinate.values()):
        del particlesDictCoordinate[(particle.getX, particle.getY)]
        particlesDictCoordinate[(particle.nextX, particle.nextY)] = particle;
        particle.getX = particle.nextX
        particle.getY = particle.nextY
        particle.getTemperature = particle.nextTemperature
        particle.getPressure = particle.nextPressure
        particle.getConcentration = particle.nextConcentration
        particle.isBurning = particle.nextIsBurning






# Display values like temperature
    mousePos = pygame.mouse.get_pos()
    mouseX = int((mousePos[0] - 72) / pixelSize)
    mouseY = int((mousePos[1] - 72) / pixelSize)

    particleTxt = particlesDictCoordinate.get((mouseX, mouseY))
    if particleTxt == None:
        txt = "Air"
    else:
        txt = str(particleTxt.getName()) +"  Temp : " + str(round(particleTxt.getTemperature, 2)) + " °C  Pressure : " + str(round(particleTxt.getPressure,2)) + " Bar"

    font = pygame.font.SysFont('Monospace Regular', 30)
    particleInfo = font.render(txt, False, (255, 255, 255))
    win.blit(particleInfo, (70, 50))

    t1 = time.time()
    if t1 - t0 < 0.016 : time.sleep(0.016-(t1-t0))
    if t0 - tBase >= 0.2 :
        t1 = time.time()
        tBase = time.time()
        fpsValue = 60 / ((t1 - t0) * 60)

    fps = font.render("Fps : "+str(round(fpsValue,1)), (50,50), (255,255,255))
    win.blit(fps, (SCREEN_WIDTH-160, 50))
    pygame.display.flip()


