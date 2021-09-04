# coding=utf-8

import pygame

pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((1280,480))

font = pygame.font.Font("KKong3.ttf", 50)
text = u'你好'
text_render = font.render(text, True, (255,255,255))
screen.blit(text_render,(300,150))

# 游戏的loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

