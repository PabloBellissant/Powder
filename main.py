# Inspiration : THE POWDER TOY
import time

import pygame
import win32api


import Enum
import particles
from particles import *
from Liquid import *
from powder import *
from gaseous import *



pixelSize = 12


pygame.init()
SCREEN_HEIGHT = pygame.display.Info().current_h
SCREEN_WIDTH = pygame.display.Info().current_w

screen = (SCREEN_WIDTH, SCREEN_HEIGHT)

win = pygame.display.set_mode(screen)




run = True
tBase = time.time()
fpsValue = 0
down = False

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

id = 0
size = 1
released = True

while run:

    mousePos = pygame.mouse.get_pos()
    mouseX = int((mousePos[0] - 72) / pixelSize)
    mouseY = int((mousePos[1] - 72) / pixelSize)

    t0 = time.time()


    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), pygame.Rect(70, 70, screen[0] - 140, screen[1] - 140), 2)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] :
            if enum.get(id+1) != None and released:
                id += 1
                released = False

        if keys[pygame.K_DOWN] :
            if enum.get(id - 1) != None and released:
                id -= 1
                released = False

        if keys[pygame.K_KP_PLUS]:
            if size < 15 and released:
                size +=1
                released = False

        if keys[pygame.K_KP_MINUS]:
            if size > 1 and released:
                size -=1
                released = False





        if not keys[pygame.K_KP_MINUS] and not keys[pygame.K_KP_PLUS] and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]: released = True





    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        if a < 0: down = True
        else: down = False


#Place particles
    if down :
        for i in range((size*2)-1):
            for p in range((size*2)-1):
                particles.create(mouseX-size+1+i, mouseY-size+1+p, id, Enum.getDefaultTemperature(id))



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
        if particle.isPowder():
            powderextPos(particle)
        if particle.isGaseous():
            gaseousNextPos(particle)










#UPDATE ALL

    toDelete = []

    for particle in list(particlesDictCoordinate.values()):

        #Delete if touch border
        if particle.getX > (SCREEN_WIDTH - 140) / pixelSize -1 : particle.delete()
        if particle.getX < 0 : particle.delete()
        if particle.getY > (SCREEN_HEIGHT - 140) / pixelSize -1 : particle.delete()
        if particle.getY < 0: particle.delete()

        particlesDictCoordinate = particlesNextCoordinate
        if particlesDictCoordinate.get((particle.getX, particle.getY)) != None :
            del particlesDictCoordinate[(particle.getX, particle.getY)]
            particlesDictCoordinate[(particle.nextX, particle.nextY)] = particle
        particle.getX = particle.nextX
        particle.getY = particle.nextY
        particle.getTemperature = particle.nextTemperature
        particle.getPressure = particle.nextPressure
        particle.getConcentration = particle.nextConcentration
        particle.isBurning = particle.nextIsBurning








# Display values like temperature

    particleTxt = particlesDictCoordinate.get((mouseX, mouseY))
    if particleTxt == None:
        txt = "Air"
    else:
        txt = str(particleTxt.getName()) +"  Temp : " + str(round(particleTxt.getTemperature, 2)) + " °C  Pressure : " + str(round(particleTxt.getPressure,2)) + " Bar"

    font = pygame.font.SysFont('Monospace Regular', 30)
    particleInfo = font.render(txt, False, (255, 255, 255))
    win.blit(particleInfo, (70, 50))

    t1 = time.time()
    if t1 - t0 < 0.0155 : time.sleep(0.0155-(t1-t0))
    if t0 - tBase >= 0.2 :
        t1 = time.time()
        tBase = time.time()
        fpsValue = 60 / ((t1 - t0) * 60)

    fps = font.render("Fps : "+str(round(fpsValue,1)), (50,50), (255,255,255))
    win.blit(fps, (SCREEN_WIDTH-160, 50))

    selectedMat = font.render("Material : " + Enum.getSimpleName(id), (50, 50), (255, 255, 255))
    win.blit(selectedMat, (SCREEN_WIDTH - 235, SCREEN_HEIGHT - 50))



    pygame.display.flip()


