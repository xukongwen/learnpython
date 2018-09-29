# -- coding: utf-8 --
# 人生第一个游戏就这么诞生了，然而并不是幻
# 昨天是1.0，今天开始各种加工，看能不能成为一个文字RPG游戏


# 版本2.0.2

from sense_hat import SenseHat # 8*8 pixel 
import time

sense = SenseHat()


import random

#初始化一个随机的HP
def int_allhp():
    com_hp=random.randint(10,20)
    user_hp=random.randint(10,20)
    return com_hp, user_hp

#攻击电脑一次
def attack_com():
    damage = random.randint(1,5)
    global c_hp #如果要调用全局变量，就要这样写，然后下面可以写对她的修改
    c_hp=c_hp-damage
    print("对敌人造成%d点伤害"%damage)
    huangdou_attack(damage)
    huangdou()
    

#显示双方最开始的HP
def show_allhp_start():
    #com_hp,user_hp = int_allhp()
    print("命运之轮开始旋转，世界初始化如下：\n")
    print("敌人初始HP：%d,玩家初始HP：%d"%(c_hp,u_hp))

#显示双方现在的HP
def show_allhp_rightnow():
    print("敌人HP：%d，玩家HP：%d"%(c_hp,u_hp))

# draw xiaohuangdou
def huangdou():
    p = (204, 0, 204) #pink
    g = (0,102,102) # green
    w=(200,200,200) # white 
    y=(204,204,0) #yellow
    e=(0,0,0)

    #sense.show_message("PHANTOM")

    pet1=[
        e, e, y, e, e, y, e, e,
        e,e,y,e,e,y,e,e,
        e,y,y,y,y,y,y,e,
        e,y,e,e,e,e,y,e,
        e,y,y,e,e,y,y,e,
        e,y,e,e,e,e,y,e,
        e,y,y,y,y,y,y,e,
        e,e,e,e,e,e,e,e
        ]

    pet2=[
        e, e, y, e, e, y, e, e,
        e,e,y,e,e,y,e,e,
        e,y,y,y,y,y,y,e,
        e,y,e,e,e,e,y,e,
        e,y,e,e,e,e,y,e,
        e,y,e,e,e,e,y,e,
        e,y,y,y,y,y,y,e,
        e,e,e,e,e,e,e,e
        ]

    for i in range(10):
        sense.set_pixels(pet1)
        time.sleep(0.1)
        sense.set_pixels(pet2)
        time.sleep(0.1)

    sense.clear()

# this is show attack 
def huangdou_attack(hp): 
    red=(255,0,0)
    sense.show_message("%d"%hp, text_colour=red)


int_allhp()
c_hp,u_hp=int_allhp() #游戏里必须有一个敌人和玩家的全局变量，否则没法弄，也没法存档
print("""
000000000000000000000000000000000000000
000000000000000000000000000000000000000
1111111111welcome to PHANTOM os11111111
1111111111欢迎来到灵魂石模拟器 11111111
000000000000000000000000000000000000000
000000000000000000000000000000000000000

        你不知道你是谁
        也没人知道你是谁
-----------------------------------------
""")




show_allhp_start()

attack_com()
show_allhp_rightnow()

temp=sense.get_temperature()

print(temp)


   
