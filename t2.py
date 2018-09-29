# -- coding: utf-8 --
# 人生第一个游戏就这么诞生了，然而并不是幻
# 昨天是1.0，今天开始各种加工，看能不能成为一个文字RPG游戏


# 版本1.0
import random
print("让我们来玩个游戏，叫做‘这都是命’")

def bidaxiao(computer, user):
    if computer > user:
        打印双方结果(computer, user)
        print_allhp(computer_hp,player_hp)
        print("完了，你输了！")

    if computer < user:
        打印双方结果(computer, user)
        print_allhp(computer_hp,player_hp)
        print("厉害，你赢了！")

    if computer == user:
        打印双方结果(computer, user)
        print_allhp(computer_hp,player_hp)
        print("啊平手了！重新开始")
        start()

def 打印双方结果(computer,user): #函数竟然可以用中文命名，太好了！
    print("电脑是：%d，而你是：%d"%(computer,user))

def int_allhp():
    computer_hp = random.randint(10,20)
    player_hp = random.randint(10,20)

def print_allhp(computer_hp,player_hp):
    print("电脑HP：%d,你的HP：%d"%(computer_hp,player_hp))

def start():
    bidaxiao(random.randint(1,9), random.randint(1,9))

int_allhp()
start()
