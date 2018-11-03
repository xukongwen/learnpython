
import pygame as pp

import phantom_core_1 as pc
import sys
import json
import pickle
import csv
import time
import random

#打开硬盘上的表格读取数据
with open('lists/list2.csv','r') as f:
    reader = csv.reader(f)
    my_list = list(reader)
    final_list = my_list[1:]#把第一行切掉


#---------------根据上帝的意志和概念创意,创建一切实例(子民),一个游戏或一个app就是实例的舞台,下面是孵化池-----------------------------------------------------

#创建玩家1号
player1 = pc.Player()

#建立游戏窗口实例
screen2 = pc.display_init(1400,1000)

#创建箱子1号
loot_box1 = pc.Loot_box(700,300,[0,1,2],20,player1)
loot_box1.make_item(final_list)
loot_box1.make_box()
player1.make_box()


#建立按钮实例
button1 = pc.Button((5,5),(100,50),screen2.Green,screen2.RED,"EXIT")
button2 = pc.Button((150,5),(100,50),screen2.Green,screen2.RED,"SAVE")
button_closebox = pc.Button((150,5),(100,50),screen2.Green,screen2.RED,"CLOSE")
b_draw = pc.Button((650,400),(150,50),screen2.Green,screen2.RED,"draw_test")
b_play = pc.Button((650,300),(150,50),screen2.Green,screen2.RED,"play_test")
b_test = pc.Button((650,500),(150,50),screen2.Green,screen2.RED,"test1")

#建立格子实例
grid2 = pc.Grid(9,50,300,300,2,screen2.Green,screen2.screen)

box1 = pc.Box(300,300,100,100,screen2.Green)


grid2.load_grid()
pp.display.set_caption("Phantom OS")

#-------------------------游戏循环主体,用各种event,让各种子民交互起来,这里是世界舞台,舞台可以有好几个--------------------------------------------

#玩家活动地图
def play():
    is_running = True
    while is_running:
        for event in pp.event.get():
                if event.type == pp.QUIT:
                    is_running = False
                elif event.type == pp.KEYDOWN:
                    if event.key == pp.K_ESCAPE:#退出游戏
                        is_running = False
                    if event.key == pp.K_i:#按i打开玩家背包
                        player1.open()
                        p_inventory()
                        
                    

                player1.event_click(event)
                loot_box1.open_box(player1.rect,event)

                if loot_box1.box_open:
                    loot_box1.open()
                    open_loot_box()


        screen2.screen.fill(screen2.WHITE)
        player1.update()

        loot_box1.draw_self(screen2.screen)
        player1.draw(screen2.screen)


        pp.display.update()
        screen2.clock.tick(60)

#玩家背包
def p_inventory():
    is_running = True
    while is_running:
        for event in pp.event.get():
                if event.type == pp.QUIT:
                    is_running = False
                elif event.type == pp.KEYDOWN:
                    if event.key == pp.K_ESCAPE:
                        is_running = False
                if button_closebox.is_clicked(event):
                    is_running = False
                
                player1.event_box(event)

            
    
                    

        screen2.screen.fill(screen2.WHITE)
            #画箱子内按钮
        pp.draw.line(screen2.screen, screen2.BLACK, [700,50],[700,950],1)
        button_closebox.update()
        button_closebox.draw(screen2.screen)

        
        player1.update_inv()#这个东西只能在循环中执行一次!需要学习!这个搞定了,下面是要只画一次.
        player1.draw_box(screen2.screen)
        player1.draw_infowin(screen2.screen)



        pp.display.update()
        screen2.clock.tick(60)



#打开箱子交互
def open_loot_box():
    is_running = True
    while is_running:
        for event in pp.event.get():
                if event.type == pp.QUIT:
                    is_running = False
                elif event.type == pp.KEYDOWN:
                    if event.key == pp.K_ESCAPE:
                        is_running = False
                if button_closebox.is_clicked(event):
                    is_running = False
                    loot_box1.box_open = False#关闭箱子

                loot_box1.event_box(event)
                loot_box1.exchange(event)
                
        screen2.screen.fill(screen2.WHITE)

        #画箱子内按钮
        pp.draw.line(screen2.screen, screen2.BLACK, [700,50],[700,950],1)
        button_closebox.update()
        button_closebox.draw(screen2.screen)
        

        #画打开箱子内的内容
        loot_box1.update_box()
        loot_box1.draw_box(screen2.screen)
        loot_box1.draw_infowin(screen2.screen)
        
        

        pp.display.update()
        screen2.clock.tick(60)


#实验的格子画画
def draw():
    is_running = True
    while is_running:
        for event in pp.event.get():#倾听所有输入事件(鼠标,键盘,手柄)
                #关闭窗口和esc事件
                if event.type == pp.QUIT:
                    is_running = False
                elif event.type == pp.KEYDOWN:
                    if event.key == pp.K_ESCAPE:
                        is_running = False

                #格子系统的格子拖拽事件
            
                grid2.event_check(event)

                #所有按钮事件
                if button1.is_clicked(event):#退出游戏
                    is_running = False
                if button2.is_clicked(event):#储存游戏
                    grid2.save_grid()
                    print('saved!')
                
            

        #---------------这里是游戏渲染区域-------------------
        #填充白色背景
        screen2.screen.fill(screen2.WHITE)
        #画出按钮
        button1.update()
        button2.update()
        button1.draw(screen2.screen)
        button2.draw(screen2.screen)
        #画出格子
        #grid1.draw_grid()
        grid2.draw_grid()
        pp.draw.line(screen2.screen, screen2.BLACK, [700,50],[700,950],1)
        
        
        #更新整体画面  
        pp.display.update()
        screen2.clock.tick(60)


#菜单主体
def menu1():
    is_running = True
    while is_running:
        for event in pp.event.get():
               
                if event.type == pp.QUIT:
                    is_running = False
                elif event.type == pp.KEYDOWN:
                    if event.key == pp.K_ESCAPE:
                        is_running = False
                
                if b_draw.is_clicked(event):
                    draw()

                if b_play.is_clicked(event):
                    play()

                if b_test.is_clicked(event):
                    open_loot_box()

        screen2.screen.fill(screen2.WHITE)

        b_draw.update()
        b_play.update()
        b_test.update()

        b_play.draw(screen2.screen)
        b_draw.draw(screen2.screen)
        b_test.draw(screen2.screen)

        pp.display.update()
        screen2.clock.tick(60)



menu1()
pp.quit()