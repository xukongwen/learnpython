# -- coding: utf-8 --

import pygame as pp
import sys
import pickle
import time

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
                #time.sleep(10)
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
                if b.x > 700 and b.y < 500:#这里放了临时的测试各自交互的，根据位置变色
            
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

#需要一个移动（拖动）的父类
#需要一个格子的夫类


class Moveable():
    #def __init__(self):

    def handle_event(self, event):

        if event.type == pp.MOUSEBUTTONDOWN:
            if self.hover:
                if event.button == 1:
                    if self.movable:
                        self.moving = True
                       
                        return True
                elif event.button == 3:
                    print(self.rect.topleft)
                    return True
                    
        if event.type == pp.MOUSEBUTTONUP:
            
            if self.hover:
                if self.movable and self.moving:
                    self.moving = False
                  
                    return True

        if event.type == pp.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
            self.pos = event.pos
                
            if self.movable and self.moving:
                self.rect.move_ip(event.rel)
                
                return True

    def info_win(self,screen):#根据情况是否显示信息块
        self.screen = screen
        if self.hover:
            #这里后面要写一些判断让信息块不要出荧幕
            info_w1 = Info_win(self.rect.x+200,self.rect.y,500,400,False,(  0,   0, 255),self.item,(255, 255, 255))
            info_w1.draw(self.screen)
        else:
            pass


class Box(Moveable):
    def __init__(self,x,y,w,h,color=(0, 100, 255),item=[]):
        self.hover = True
        self.color = color
        self.rect = pp.Rect(x, y, w, h)
        self.image = pp.Surface((w,h))
        self.image.fill(self.color)
        self.item = item
    
        self.moving = False
        self.movable = True

        
    
        pp.draw.rect(self.image, self.color, self.rect)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)



class Info_win(Moveable):
    def __init__(self, x, y, width, height, movable=True, color=(0,0,0), text_list=[], text_color=(0,0,0)):
        self.hover = True
        self.moving = False
        self.movable = movable
        self.color = color
        self.text_color = text_color
        row = 5

        self.rect = pp.Rect(x, y, width, row+95)
        self.image = pp.Surface((width,height))
        self.image.fill(self.color) 
        
        self.x = x
        self.y = y
        self.font = pp.font.Font('华文宋体.ttf', 25)#中文字体需要这样写，而不是sys.font
        self.width =width
        self.height = height
        self.text_list = text_list

        for i in self.text_list:#我草这里竟然成功了！这里是把list中的属性按行分别读出来然后显示出来
            text_image = self.font.render(str(i), True, self.text_color)
            text_rect = text_image.get_rect()
            row += 35
            self.image.blit(text_image, (10, row ,*text_rect.size))

        pp.draw.rect(self.image,self.color,self.rect)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)



#按钮的本尊
class Button(object):
    def __init__(self, pos, size, color, h_color,text):

        self.image_normal = pp.Surface(size)
        self.image_normal.fill(color)

        self.image = self.image_normal
        self.rect = pp.Rect((0,0),size)
    
        self.image_hovered = pp.Surface(size)
        self.image_hovered.fill(h_color)

        font = pp.font.Font(None,24)
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
                return self.rect.collidepoint(event.pos)#事件
                
#玩家的本尊
class Player():
    def __init__(self):
        self.image = pp.Surface((50,100))
        self.image.fill((   0, 255,   0))
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 500
        #下面设这些开关很好用，所有的update在一个地方，其他按键只是激活开关
        self.m_up = False
        self.m_down = False
        self.m_left = False
        self.m_right = False
      

#接收键盘信息
    def event_click(self,event):
            if event.type == pp.KEYDOWN:
                if event.key == pp.K_UP:
                    self.m_up = True
                if event.key == pp.K_DOWN:
                    self.m_down = True
                if event.key == pp.K_RIGHT:
                    self.m_right = True
                if event.key == pp.K_LEFT:
                    self.m_left = True
            
            elif event.type == pp.KEYUP:
                if event.key == pp.K_UP:
                    self.m_up = False
                if event.key == pp.K_DOWN:
                    self.m_down = False
                if event.key == pp.K_RIGHT:
                    self.m_right = False
                if event.key == pp.K_LEFT:
                    self.m_left = False

#接受到开关信息后更新player的位置           
    def update(self):
        if self.m_up == True:
            self.rect.y -= 10
            if self.rect.y < 0:
                self.rect.y = 1000

        if self.m_down == True:
            self.rect.y += 10
            if self.rect.y > 1000:
                self.rect.y = 0
            
        if self.m_left == True:
            self.rect.x -= 10
            if self.rect.x < 0:
                self.rect.x = 1400

        if self.m_right == True:
            self.rect.x += 10
            if self.rect.x > 1400:
                self.rect.x = 0
      




    def draw(self, screen):
        screen.blit(self.image, self.rect)


#物品类
class Item():
    dur=0
    def __init__(self,name,item_type,wuxing,n_name,num,weight,price,att,dur,rare,player_dis):
        self.name = name
        self.type = item_type
        self.wuxing = wuxing
        self.n_name = n_name
        self.num = num
        self.weight = weight
        self.price = price
        self.att = att
        self.dur = dur  
        self.rare = rare
        self.player_dis = player_dis

    def info(self):#存成一个自己的list
        item_info_list = [self.name,self.type,self.wuxing,self.n_name,self.num,self.weight,self.price,self.att,self.dur,self.rare,self.player_dis]
        return item_info_list

    def fixdur(self):#临时的修理
        self.dur = int(self.dur) + 10
        return self.dur

    def print_info(self):#临时的打印所有信息
        print_info = self.name,self.type,self.wuxing,self.n_name,self.num,self.weight,self.price,self.att,self.dur,self.rare,self.player_dis
        return print_info


#写了一个箱子的类,用来事先存放东西,然后可以拿走,和放入
class Loot_box():
    def __init__(self,item_list,item_num):
        self.item_list = item_list#这里输入是一个列表,就可以同时输入n个物品!
        self.item_num = item_num
        self.loot_box = []#本箱子的最终list
        self.d_box = []
        

    #box1 = pc.Box(300,300,100,100,screen2.Green)
    def make_box(self):#制作物品gird清单
        for i, r in enumerate(self.loot_box):
            self.d_box.append(Box((100+i*60),300,50,50,(0, 255,   0),r))
    
    def draw_box(self, screen):#根据list数量画出物品
        for d in self.d_box:
            d.draw(screen)

    def event_box(self,event):#给每个物品添加鼠标移动相关交互
        for d in self.d_box:
            d.handle_event(event)

    def draw_infowin(self,screen):#这里以后改到box里面实现
        for d in self.d_box:
            d.info_win(screen)





    def make_item(self,final_list):
        for i in self.item_list:#根据输入的list,把物品装入
            temp_item = Item(*final_list[int(i)])#类里面可以调用其他的类,这里是展开list列表,填入属性
            self.loot_box.append(temp_item.info())#加入根据编号的物品进入箱子

    def take_item(self):#拿走东西,并添加给玩家,一定要先给再删除
        player_inventory.append(self.loot_box[2])
        del self.loot_box[2]

    def add_item(self):#玩家向箱子添加
        self.loot_box.append(player_inventory[0])
        del player_inventory[0]

    def show_boxname(self):
        boxname = 'box'
        return boxname




