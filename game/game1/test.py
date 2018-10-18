import pygame as pp
import random
import os

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)        
RED   = (255,   0,   0)
Green = (  0, 255,   0)
BLUE  = (  0,   0, 255)
YELLOW = (255,255,   0)

s_w = 1000
s_h = 700
SCREEN_size = (s_w,s_h)
s_color = WHITE



pp.display.init()#最先要初始化,别的都别说

is_running = True
screen = pp.display.set_mode((SCREEN_size))
pp.display.set_caption("Phantom")
#这个学到了,解决相对路径的问题
basePath = os.path.dirname(__file__)
dudePath = os.path.join(basePath, "s2.bmp")

image1 = pp.image.load(dudePath)
pp.display.set_icon(image1)

image1_rect = image1.get_rect()
screen_rect = screen.get_rect()
image1_rect.x = 500
image1_rect.y = 350
move_up = False

while is_running:
    r_color = [random.randint(0, 255) for _ in range(3)]

    screen_rect = screen.get_rect()
    for event in pp.event.get():
        if event.type == pp.QUIT:
            is_running = False

        elif event.type == pp.KEYDOWN:
            if event.key == pp.K_ESCAPE:
                is_running = False

            elif event.key == pp.K_5:
                s_color = r_color

            elif event.key == pp.K_6:
                pp.display.toggle_fullscreen()

            elif event.key == pp.K_7:
                pp.image.save(screen,"/home/xukongwen/github/learnpython/game/game1/hi.png")

            elif event.key == pp.K_UP:
                image1_rect.y -= 10
                if image1_rect.y < 0:
                    image1_rect.y = 650


        

    
            

 
    
    
    screen.fill((s_color))
    screen.blit(image1,image1_rect)
    






    pp.display.update()