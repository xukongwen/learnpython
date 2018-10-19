# -- coding: utf-8 --

import pygame as pp
import sys
import pickle

#-------------------------------------------类就是上帝创世区域,全部是抽象设计,没有实体--------------------------------------------------------------------------

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
        self.load_s = False
        self.flag = True

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
                #if self.rects[self.selected].x > 700:
                #print(self.selected, self.rects[self.selected])

        

    #画出格子,根据读档
    def draw_grid(self):
        if self.load_s == True and self.flag:
            self.flag = False
            pickle_in = open("saves/save_2","rb")
            load_file = pickle.load(pickle_in)
            self.rects = load_file
            for b in self.rects:
                pp.draw.rect(self.sc, self.b_color, b)
               
        if self.load_s != True:
            self.flag = True
        else:
            for b in self.rects:
                if b.x > 700 and b.y < 500:
                    #self.b_color = (255,0,0)
                    #print(b)
                    pp.draw.rect(self.sc, (255,0,0),b)
                elif b.y > 500 and b.x > 700:
                    pp.draw.rect(self.sc, ( 0,  0, 255),b)
                else: 
                    pp.draw.rect(self.sc, self.b_color, b)

    #读档功能
    def load_grid(self):
        pickle_in = open("saves/save_2","rb")
        load_file = pickle.load(pickle_in)
        
        self.load_s = True
        for b in load_file:
            pp.draw.rect(self.sc, self.b_color, b)

    #储存功能
    def save_grid(self):
        pickle_out = open("saves/save_2","wb")
        pickle.dump(self.rects, pickle_out)
       
        pickle_out.close()


        


#按钮的本尊
class Button(object):
    def __init__(self, pos, size, color, h_color,text):

        self.image_normal = pp.Surface(size)
        self.image_normal.fill(color)

        self.image = self.image_normal
        self.rect = pp.Rect((0,0),size)
    
        self.image_hovered = pp.Surface(size)
        self.image_hovered.fill(h_color)

        font = pp.font.Font(None,32)
        text = font.render(text, True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image_normal.blit(text, text_rect)
        self.image_hovered.blit(text, text_rect)

        self.rect.topleft = pos

        self.hovered = False
        self.clicked = False

    def update(self):#更新鼠标划过状态
        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal


    def draw(self, screen):#画按钮
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pp.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pp.MOUSEBUTTONDOWN:
            if self.hovered:
            
            #if event.button == 1:
                
                return self.rect.collidepoint(event.pos)#事件
                





