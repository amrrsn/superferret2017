# -*- coding: utf-8 -*-

import pygame
import sys
from random import randint
from time import sleep
from pygame.locals import *

wwidth = 800
wheight = 600
maxx = 0
FPS = 60
game = True
player_width = 50
player_height = 50
frame = 1
x_vel = 0
y_vel = 0
x = 0
y = wheight - 10 - player_height
jumping = False
on = ''
dir = "right"
coin_count = 0
sword = 0

# entity heights
spike_height = 20
enemy_height = 50
boss_height = 100
coin_height = 25
sword_height = 24

# load images
left = pygame.image.load("Left looking.png")
right = pygame.image.load("Right Looking.png")
platimg = pygame.image.load("Brick.png")
bg = pygame.image.load("Sky.png")
eneimg = pygame.image.load("coyote.png")
floimg = pygame.image.load("brickfloor.png")
bossimg = pygame.image.load("brickmonstermaybe.png")
ss = pygame.image.load("titlescreenbackground.png")
titley = pygame.image.load("titleyellow.png")
titlem = pygame.image.load("titlemagenta.png")
ends = pygame.image.load("end.png")
coinimg = pygame.image.load("coin.png")
swordimg = pygame.image.load("sword.png")

# mouse stuff
mouse_x = 0
mouse_y = 0
mousedown = False

pygame.init()
w = pygame.display.set_mode([wwidth, wheight])

f = pygame.font.SysFont("comicsansms",30)
play_text = f.render("Play",True,[0,0,0])
play_text_display = play_text.get_rect()
quit_text = f.render("Quit",True,[0,0,0])
quit_text_display = quit_text.get_rect()
h = pygame.font.SysFont("comicsansms",18)
directions1 = h.render("Directions: Use the arrow keys to move the ferret.",True,[0,0,0])
directions2 = h.render("Up is jump and left and right move",True,[0,0,0])
directions3 = h.render("the ferret left and right, respectively.",True,[0,0,0])
directions1_display = directions1.get_rect()
directions1_display.center = [215,10]
directions2_display = directions2.get_rect()
directions2_display.center = [145,30]
directions3_display = directions3.get_rect()
directions3_display.center = [165,50]

pygame.display.set_caption("Super Ferret")

platforms = [[450, 520],
             [650,520],
             [900,520],
             [1000,450],
             [1100,380],
             [1400,520],
             [1600,520],
             [1700,450],
             [1800,520],
             [1900,450],
             [2100,450],
             [2300,520],
             [2500,450],
             [2600,520],
             [2800,520],
             [2900,450],
             [3000,380],
             [3300,520],
             [3400,450],
             [3500,380],
             [3600,310],
             [4000,520],
             [4100,450],
             [4200,380],
             [4300,310],
             [4400,240],
             [4700,520],
             [4900,520],
             [5400,520],
             [5500,450],
             [5600,380],
             [5700,310],
             [5800,240]]
spikes = [580,
          2030,
          2530,
          3130,
          3230,
          3830,
          4630,
          5030,
          5230,
          5930,
          6030,
          6130,
          6230,
          6330,
          6430]
pits = [1100,
        1500,
        1600,
        2200,
        4300,
        4800,
        5400,
        6500,
        6600,
        6700,
        6800,
        6900,
        7000]
enemies = [[780, wheight - 10 - enemy_height],
           [1800,520 - enemy_height],
           [2410,wheight - 10 - enemy_height]]
bossenemies = [[1250,wheight - 10 - boss_height,1],
               [4500,wheight - 10 - boss_height,1]]
coins = [[1038,wheight - 15 - coin_height],
         [1738,wheight - 15 - coin_height],
         [2138,wheight - 15 - coin_height],
         [2538,450 - 15 - coin_height],
         [3338,520 - 15 - coin_height],
         [4038,520 - 15 - coin_height],
         [4238,wheight - 15 - coin_height],
         [4738,520 - 15 - coin_height]]
swords = [[1140,380 - 15 - sword_height],
          [2140,450 - 15 - sword_height]]

keys = []

#pygame.mixer.music.load("titletheme.mp3")
#pygame.mixer.music.play(-1)

while True:
    w.blit(ss, [0,0])

    for e in pygame.event.get():
        if e.type == QUIT: pygame.quit(), sys.exit()
        elif e.type == MOUSEBUTTONDOWN: mousedown = True
        elif e.type == MOUSEBUTTONUP: mousedown = False
        elif e.type == MOUSEMOTION:
            mouse_x = e.pos[0]
            mouse_y = e.pos[1]

    if mouse_x > 200 and mouse_x < 595 and mouse_y > 20 and mouse_y < 175: w.blit(titlem, [200,20])
    else: w.blit(titley, [200,20])
    play = pygame.draw.rect(w, [255,255,0], [(wwidth - 100) / 2,(wheight - 50) / 2,100,50])
    quitbtn = pygame.draw.rect(w, [255,255,0], [play.x,play.y + play.height + 10,100,50])
    play_text_display.center = [play.x + play.width / 2,play.y + play.height / 2]
    quit_text_display.center = [quitbtn.x + quitbtn.width / 2,quitbtn.y + quitbtn.height / 2]
    w.blit(play_text, play_text_display)
    w.blit(quit_text, quit_text_display)

    if mousedown and mouse_x > play.x and mouse_x < play.x + play.width and mouse_y > play.y and mouse_y < play.y + play.height: break
    if mousedown and mouse_x > quitbtn.x and mouse_x < quitbtn.x + quitbtn.width and mouse_y > quitbtn.y and mouse_y < quitbtn.y + quitbtn.height: pygame.quit(), sys.exit()
    pygame.display.update()
    sleep(1 / FPS)

#pygame.mixer.music.stop()
#pygame.mixer.music.load("mariotheme.mp3")
#pygame.mixer.music.play(-1)

while game:
    w.blit(bg, [0,0])
    if abs(x) < 10: w.blit(directions1, directions1_display), w.blit(directions2, directions2_display), w.blit(directions3, directions3_display)

    for e in pygame.event.get():
        if e.type == QUIT: pygame.quit(), sys.exit()
        elif e.type == KEYDOWN and not e.key in keys: keys.append(e.key)
        elif e.type == KEYUP and not e.key == K_p: keys.remove(e.key)

    if dir == "right": player = w.blit(right, [(wwidth - player_width) / 2,y])
    else: player = w.blit(left, [(wwidth - player_width) / 2,y])
    floor = w.blit(floimg, [0,wheight - 10])

    onground = False

    for p in platforms:
        if p[0] + x < wwidth and p[0] + x > -100:
            plat = w.blit(platimg, [p[0] + x,p[1]])
            if player.colliderect(plat) and player.y + (player.height * 0.75) < plat.y:
                onground = True
                on = plat
                jumping = False
                y_vel = 0
                y = plat.y - player_height + 1

    for s in spikes:
        if s + x < wwidth and s + x > -100:
            spike = pygame.draw.polygon(w, [255,0,0], [[s + x,wheight - 10],[s + x + 10,wheight - 10 - spike_height],[s + x + 20,wheight - 10],[s + x + 30,wheight - 10 - spike_height],[s + x + 40,wheight - 10]])
            if player.colliderect(spike) and sword == 0: game = False
            elif player.colliderect(spike):
                sword -= 1
                spikes.remove(s)
                coin_count += 10

    for pit in pits:
        if pit + x < wwidth and pit + x > -100:
            pi = pygame.draw.rect(w, [144,203,243], [pit + x,wheight - 10,100,10])
            if player.colliderect(pi): game = False

    for e in enemies:
        if e[0] + x < wwidth and e[0] + x > -100:
            enemy = w.blit(eneimg, [e[0] + x,e[1]])
            if player.colliderect(enemy) and sword == 0: game = False
            elif player.colliderect(enemy):
                sword -= 1
                enemies.remove(e)
                coin_count += 50

    for be in bossenemies:
        if be[0] + x < wwidth and be[0] + x > -100:
            boss = w.blit(bossimg, [be[0] + x,be[1]])
            if be[1] + boss_height > wheight - 10: be[2] = -1
            elif be[1] + boss_height < wheight - 40: be[2] = 1
            if frame % 5 == 0: be[1] += be[2]
            if player.colliderect(boss) and sword == 0: game = False
            elif player.colliderect(boss):
                sword -= 1
                bossenemies.remove(be)
                coin_count += 100

    for c in coins:
        if c[0] + x < wwidth and c[0] + x > -100:
            coin = w.blit(coinimg, [c[0] + x,c[1]])
            if player.colliderect(coin):
                coin_count += 500
                coins.remove(c)

    for swo in swords:
        if swo[0] + x < wwidth and swo[0] + x > -100:
            d = w.blit(swordimg, [swo[0] + x,swo[1]])
            if player.colliderect(d):
                sword += 1
                swords.remove(swo)

    if sword > 0: w.blit(swordimg, [wwidth - 25,5])

    if player.colliderect(floor):
        onground = True
        on = floor
        jumping = False
        y_vel = 2
        y = floor.y - player_height + 1

    if (K_UP in keys or K_w in keys) and onground and not jumping:
        jumping = True
        oy_vel = 50
        oframe = frame - 1
        y_vel = oy_vel * (frame - oframe) / 3 - 5 * pow((frame - oframe) / 3,2)
        oy = y
    if (K_LEFT in keys or K_a in keys) and onground:
        x_vel += 2
        dir = "left"
    if (K_RIGHT in keys or K_d in keys) and onground:
        x_vel -= 2
        dir = "right"
    if K_p in keys: sword = 1

    if jumping:
        y = oy - y_vel
        y_vel = oy_vel * (frame - oframe) / 3 - 5 * pow((frame - oframe) / 3,2)
    if not onground and not jumping:
        y += y_vel
        y_vel += 1
    if x_vel != 0:
        x += x_vel
        if onground: x_vel *= 0.75
        elif jumping: x_vel *= 0.99
        else: x_vel *= 0.95

    if x > 0: x = 0

    if abs(x) > maxx: maxx = round(abs(x))

    pygame.display.update()
    sleep(1 / FPS)
    frame += 1

#pygame.mixer.music.stop()
#pygame.mixer.music.load("gameover.mp3")
#pygame.mixer.music.play()
with open("highscore.txt","r+") as hi:
    highscore = hi.read()
if int(highscore) < (maxx + coin_count + sword) * 10:
    open("highscore.txt","w").close()
    s = open("highscore.txt","w")
    s.write(str((maxx + coin_count + sword) * 10))
    highscore = (maxx + coin_count + sword) * 10
w.blit(ends, [0,0])
score = f.render("Your Score: " + str((maxx + coin_count + sword) * 10),True,[230,200,18])
hiscore = f.render("Highscore: " + str(highscore),True,[230,200,18])
score_display = score.get_rect()
score_display.center = [wwidth / 2,wheight / 2 - 140]
hiscore_display = hiscore.get_rect()
hiscore_display.center = [wwidth / 2,wheight / 2 - 105]
w.blit(score, score_display)
w.blit(hiscore, hiscore_display)
pygame.display.update()
while True:
    for e in pygame.event.get():
        if e.type == QUIT or e.type == MOUSEBUTTONDOWN:
            #pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
