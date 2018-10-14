# -- coding: utf-8 --
import pygame as pp

import phantom_core_1 as pc
import sys


is_running = True
list1 = []
list2 = []
screen2 = pc.display_init(1600,1400)
grid2 = pc.Grid(9,50,300,300,2,screen2.Green,screen2.screen)
grid1 = pc.Grid(9,30,900,300,1,screen2.RED,screen2.screen)

while is_running:
    for event in pp.event.get():
 
       
            if event.type == pp.QUIT:
                sys.exit()
 
            elif event.type == pp.KEYDOWN:
                if event.key == pp.K_ESCAPE:
                    sys.exit()
                    #is_running = False
            grid1.event_check(event)
                
            grid2.event_check(event)
             
    


    screen2.screen.fill(screen2.WHITE)
    grid1.draw_grid()
    grid2.draw_grid()
    
    
       
    pp.display.update()

    screen2.clock.tick(60)
    
pp.quit()