# -- coding: utf-8 --
#学习class
#pygame终于可以输入和显示中文了!

import time
import random
import csv
import pygame

clock = pygame.time.Clock()

WIDTH = 2000  
HEIGHT = 1300 
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
sp = pygame.sprite.Sprite
all_sprites = pygame.sprite.Group()
pygame.mixer.init()  # 声音
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Phantom Game")
clock = pygame.time.Clock()


class Gird_box(sp):
    def __init__(self,pos_x,pos_y,color):#color这里如果写'r',就是随机!
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.color = color
        self.r_color = [random.randint(0, 255) for _ in range(3)]
        if self.color == 'r':
            self.image.fill(self.r_color)
        else:
            self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.center = (self.pos_x, self.pos_y)

    def makegrid(self):
        for box in range(0,19):#我曹,我竟然做出来了!!!
            for box in range(0,19):#先画出一行
                box_in.pos_x += 11
                box = Gird_box(box_in.pos_x, box_in.pos_y,box_in.color)
                all_sprites.add(box)
            box_in.pos_y += 11#再画向下排一行
            box_in.pos_x = 200#但x要归零!
    

        
    


#显示文字的模块,支持中文
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font("华文宋体.ttf", 40)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



box_in = Gird_box(200,200,GREEN)
box_in.makegrid()


running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
            # check for closing window
        if event.type == pygame.QUIT:
            running = False
        
    
        
    all_sprites.update()#sp先update

    screen.fill(WHITE)#画背景
    all_sprites.draw(screen)#在背景上画所有的sp
    draw_text(screen, '你好', 18, WIDTH / 2, 10)
    pygame.display.flip()

    pygame.display.update()
pygame.quit()
    




