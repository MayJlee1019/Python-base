#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2019/1/22 8:48
# @Author : wangjun
# @File   : snow.py
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

SIZE = (900, 700)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('下雪了')

background = pygame.image.load('tupian.jpg')

snow = []

for i in range(300):
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(3, 8)
    snow.append([x, y, speedx, speedy])

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0, 0))

    for i in range(len(snow)):
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])

        snow[i][0] += snow[i][2]
        snow[i][1] += snow[i][3]

        if snow[i][1] > SIZE[1]:
            snow[i][1] = random.randrange(-50, -10)
            snow[i][0] = random.randrange(0, SIZE[0])

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
