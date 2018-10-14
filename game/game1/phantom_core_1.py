# -- coding: utf-8 --

import pygame as pp
import sys

#下面是设定游戏窗口相关
class display_init():
    def __init__(self,w,h):
        self.BLACK = (  0,   0,   0)
        self.WHITE = (255, 255, 255)
        
        self.RED   = (255,   0,   0)
        self.Green = (  0, 255,   0)
        self.BLUE  = (  0,   0, 255)
        self.YELLOW = (255,255,   0)
        
        self.w  = w
        self.h = h

        pp.init()
        
        self.screen = pp.display.set_mode((self.w, self.h))
        self.screen_rect = self.screen.get_rect()
        self.clock = pp.time.Clock()
        
#定义grid相关
class Grid():
    #格子数量(暂时是横竖相等),格子大小,格子位置,格子中间空隙大小,格子颜色,选择窗口
    def __init__(self,num,b_size,g_x,g_y,g_space,b_color,sc):
        self.selected_offset_x = 0
        self.selected_offset_x = 0
        self.b_size = b_size
        self.g_x = g_x
        self.g_y = g_y
        self.b_color = b_color
        self.g_space = g_space
        self.rects = []
        self.sc = sc
        self.num = num

        #创建所有格子
        for x in range(self.num):
            for y in range (self.num):
                self.rects.append(pp.Rect(x*(self.b_size+self.g_space)+self.g_x, y*(self.b_size+self.g_space)+self.g_y, self.b_size, self.b_size ))
        self.selected = None

    #检查格子触发事件,和激活按下格子事件
    def event_check(self,event):
        if event.type == pp.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, r in enumerate(self.rects):
                    #是否在格子内按下鼠标
                    if r.collidepoint(event.pos):
                        #这里是任何在方块内按下可以触发的事件 
                        self.selected = i 
                        self.selected_offset_x = r.x - event.pos[0]#计算出鼠标在格子内的偏移
                        self.selected_offset_y = r.y - event.pos[1]

        elif event.type == pp.MOUSEBUTTONUP:
            if event.button == 1:
                self.selected = None

         #让格子随鼠标移动      
        elif event.type == pp.MOUSEMOTION:
            if self.selected is not None: 
                self.rects[self.selected].x = event.pos[0] + self.selected_offset_x
                self.rects[self.selected].y = event.pos[1] + self.selected_offset_y 
    #画出格子
    def draw_grid(self):
        for b in self.rects:
            pp.draw.rect(self.sc, self.b_color, b)
        






