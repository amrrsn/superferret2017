# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:41:49 2017

@author: Spartyk12
"""

import pygame
from pygame.locals import *

pygame.init()

fps = 60

wwidth = 800
wheight = 600


w = pygame.display.set_mode([wwidth, wheight])
pygame.display.set_caption("Triangle?")

fpsClock = pygame.time.Clock()

while True:
    
    w.fill([255,255,255])
    pygame.draw.polygon(w, [0,0,0], [((0),(wheight)), (20, wheight), (10, wheight-20)])
    for event in pygame.event.get():
        #print(event)
        if event.type == QUIT:
            pygame.quit()
    pygame.display.update()
    fpsClock.tick(fps)
    
    