# -- coding: utf-8 --
#学习class

#类可以定义类的特定属性,以及内部可运行的各种函数(功能)
import time
import random
import csv

#读取csv列表
with open('list1.csv','r') as f:
    reader = csv.reader(f)
    my_list = list(reader)
    final_list = my_list[1:]#把第一行切掉

print(final_list)

# 忽略这里,是胡闹的
class Dao():
    def __init__(self):
        pass

class Yin(Dao):
    def __init__(self):
        super.__init__()
        pass

class Yang(Dao):
    def __init__(self):
        super.__init__()
        pass




class Item():
    def __init__(self,name,num,type):
        self.name = name
        self.num = num
        self.type = num

class Sword(Item):
    def __init__(self,name,num,type):
        super.__init__(name,num,type)
        attack = att
        durable = dur
        weight = wei
        price = pri

    def fix():
        durable = durable + 10

class Herbs(Item):
    def __init__(self,name,num,type):
        super.__init__(name,num,type)
        useage = use
        price = pri

    def eat():
        print('+10HP')


    
