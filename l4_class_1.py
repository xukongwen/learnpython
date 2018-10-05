# -- coding: utf-8 --
#学习class

#类可以定义类的特定属性,以及内部可运行的各种函数(功能)


class Pig():
    #定义类的各种属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #类里面可以执行的函数
    def sit(self):
        print(self.name + "坐下了")

    def eat(self):
        print(self.name + "开始吃")



class Item():
    def __init__(self,name,price,weight,rare,durable):
        self.name = name
        self.price = price
        self.weight = weight
        self.rare = rare
        self.durable = durable

    def display_iteminfo(self):
        print(self.name+":价格:"+str(self.price)+"重量:"+str(self.weight)+'稀有度:'+self.rare+'耐久:'+str(self.durable))

mypig = Pig('xukongwen',12)
mypig.sit()


my_sowrd = Item('大剑',250,100,'破损',20)
my_sowrd.display_iteminfo()

#hi
#sdfsd
