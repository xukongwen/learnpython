# -- coding: utf-8 --
import pygame as pp

import phantom_core_1 as pc
import sys
import json
import pickle


is_running = True
screen2 = pc.display_init(1600,1300)

button1 = pc.Button((5,5),(100,50),screen2.Green,screen2.RED,"EXIT")
button2 = pc.Button((150,5),(100,50),screen2.Green,screen2.RED,"SAVE")


grid2 = pc.Grid(9,50,300,300,2,screen2.Green,screen2.screen)
grid1 = pc.Grid(1,30,900,300,1,screen2.RED,screen2.screen)

grid2.load_grid()



while is_running:
    for event in pp.event.get():
 
       
            if event.type == pp.QUIT:
                
                is_running = False
                
 
            elif event.type == pp.KEYDOWN:
                if event.key == pp.K_ESCAPE:
                    is_running = False
            grid1.event_check(event)
                
            grid2.event_check(event)

            if button1.is_clicked(event):
                is_running = False

            if button2.is_clicked(event):
                grid2.save_grid()
                print('saved!')
             
    


    screen2.screen.fill(screen2.WHITE)
    button1.update()
    button2.update()
    button1.draw(screen2.screen)
    button2.draw(screen2.screen)
    grid1.draw_grid()
    grid2.draw_grid()
    
    
       
    pp.display.update()


    screen2.clock.tick(60)




pp.quit()