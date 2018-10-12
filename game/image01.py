# -- coding: utf-8 --
#学习pygame基础交互和画图
#鼠标交互,中文显示


#整个主要学到几个事, 1 游戏有一个主进程一般是main(),这里又有一个事件进程,这里是
#等待玩家的输入 然后主进程根据玩家的输入做出画面的更新,在这些进程之前是必要的初始化
#然后这些东西组成一个类,或者说就是整个游戏本身


import os
import sys
import random
import pygame as pp

CAPTION = 'PHANTOM'
SCREEN_SIZE = (1700,1000)

class Player(object):#玩家操控的东西本身,包括一个方块和一个文字
    SIZE = (200,200)
    def __init__(self,pos):
        self.rect = pp.Rect((0,0),Player.SIZE)#画正方形
        self.rect.center = pos
        self.text, self.text_rect = self.setup_font()
        self.click = False

    def setup_font(self):#字体和写字的内容
        font = pp.font.Font("华文宋体.ttf", 40)#中文字体就是这样设定
        message = "欢迎,这是PHANTOM OS"
        label = font.render(message, True, pp.Color("black"))#文字本身
        label_rect = label.get_rect()#这里似乎是给出了文字所占的方块
        return label, label_rect#这里返回的两个值定义了上面的text和text_rect

    def check_clikc(self,pos):#检查鼠标是否在方块内按下
        if self.rect.collidepoint(pos):
            self.click = True
            pp.mouse.get_rel()#这个好像是获得鼠标的位移,图像跟随鼠标全靠的是这个
            self.color = [random.randint(0, 255) for _ in range(3)]#上面很有意思,在整个[]list里,整个方式就是做出了三组随机的颜色 _ 是临时一个变量
            return self.click

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pp.mouse.get_rel())#移动方块到鼠标的地方
            self.rect.clamp_ip(screen_rect)#在那个里面移动,就是在窗口里移动
        self.text_rect.center = (self.rect.centerx, self.rect.centery+0)#更新文字的坐标

    def draw(self, surface):#分别画出方块和文字
        surface.fill(pp.Color("red"),self.rect)
        surface.blit(self.text, self.text_rect)

class App(object):#总程序本身
    def __init__(self):
        self.screen = pp.display.get_surface()#给出显示的窗口
        self.screen_rect = self.screen.get_rect()#窗口的矩形
        self.clock = pp.time.Clock()#固定帧率
        self.fps = 60
        self.done = False
        self.keys = pp.key.get_pressed()#所有玩家触动的按键
        self.color = pp.Color("white")
        self.player = Player(self.screen_rect.center)#把player放在窗口的中间

    def event_loop(self):#这个事件循环是程序里所有逻辑的触发,没有任何绘图的东西,一个游戏只能有一个eventloop
        for event in pp.event.get():#从事件列表中抓取事件
            #print(event)
            if event.type == pp.QUIT or self.keys[pp.K_ESCAPE]:#退出游戏的触发
                self.done = True
            elif event.type == pp.MOUSEBUTTONDOWN and event.button == 1:
                
                self.player.check_clikc(event.pos)#秘密都在这里,event.pos其实打印一下event就全明白了,event是一个动态的字典!只要鼠标和键盘动,它就会变化!
                change = self.player.check_clikc(event.pos)#这里初步实现了按钮的功能!

                if change == True:
                    self.color = [random.randint(0, 255) for _ in range(3)]
                else:
                    pass

            elif event.type == pp.MOUSEBUTTONUP and event.button ==1:
                self.player.click = False
                
            elif event.type in (pp.KEYUP, pp.KEYDOWN):
                self.keys = pp.key.get_pressed()

            
    
    def render(self):#这里是所有的画面相关
        self.screen.fill(self.color)#给出颜色
        self.player.draw(self.screen)
        pp.display.update()

    def main_loop(self):#这里只是管理进程,而不做任何具体事
        while not self.done:#游戏的loop在这里
            self.event_loop()#先看玩家输入了什么再做决定
            self.player.update(self.screen_rect)#根据玩家操控做出相应update
            self.render()#渲染出画面
            self.clock.tick(self.fps)

def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'#把窗口弄到中间
    pp.init()#pygame初始化
    pp.display.set_caption(CAPTION)
    pp.display.set_mode(SCREEN_SIZE)
    App().main_loop()#开始主进程
    pp.quit()
    sys.exit()

if __name__ == "__main__":#整个东西是让其他程序如果调用自己的话,main()不运行,而变为一个模块
    main()

