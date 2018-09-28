# -- coding: utf-8 --
# 人生第一个游戏就这么诞生了，然而并不是幻
import random
print("让我们来玩个游戏")

def bidaxiao(computer, user):
    if computer > user:
        print("完了，你输了！")

    if computer < user:
        print("厉害，你赢了！")

    if computer == user:
        print("啊平手了！重新开始")
        start()

def start():
    bidaxiao(random.randint(1,9), int(input("输入1-9：")))

start()
