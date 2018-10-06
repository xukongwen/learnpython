# -- coding: utf-8 --
#学习class

#类可以定义类的特定属性,以及内部可运行的各种函数(功能)
import time;
import random

player_inventory = []

home_box = []



#每一把独特大剑的属性
item_l_gt_s_01 = [
'最终的把手' ,20, 50, '平庸',50,
]

item_l_gt_s_02 = [
'清凉之手',20,50,'奇怪','破损',
]

#所有大剑的集合
item_list_swords =[item_l_gt_s_01,item_l_gt_s_02

]


# 放置各种名词
name_list_a = [
    '时间','人类','同化','物化','无物','庄周','何以',
    '情况','类型'
]

# 放置各种形容词到达"什么的什么"
name_list_b = [
    '残酷','标准','没有序列','含糊不清','暗淡','恬淡',
    '经过','死亡','渐进','无限'
]

# 耐久度的词语
durable_list_a =[
    '锋利','饱满','结实','松垮','不堪一击',

]
#设置一个空随机箱子
random_lootbox = []


#随机造名字
def randname():
    maxlist_a = len(name_list_a)-1#这里一定要-1
    maxlist_b = len(name_list_b)-1
    randomlist_a = random.randint(0,maxlist_a)
    randomlist_b = random.randint(0,maxlist_b)
    new_name_a = name_list_a[randomlist_a]
    new_name_b = name_list_b[randomlist_b]

    new_random_name = new_name_b+"的"+new_name_a
    
    return new_random_name


#randname()
#p=randname()
#print(p)



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

#实验一下随机属性和随机名字,貌似成功了,需要用函数的返回值
class Item():
    def __init__(self,name,price,weight,rare,durable):
        self.name = name
        self.price = price
        self.weight = weight
        self.rare = rare
        self.durable = durable

    def display_iteminfo(self):
        output_info1 = self.name+":价格:"+str(self.price)+"重量:"+str(self.weight)+'稀有度:'+self.rare+'耐久:'+str(self.durable)
        return output_info1

    def display_name(self):
        self.name = randname()
        self.price = random.randint(0,101)
        self.weight = random.randint(0,51)
        output_info = self.name+':'+'价格:'+str(self.price)+" "+"重量:"+str(self.weight)
        return output_info

class Great_sword(Item):
    def __init__(self,name,price,weight,rare,durable):
        super().__init__(name,price,weight,rare,durable)
        self.sowrdname = '大剑'

    def onename(self):
        one_name = self.sowrdname
        return one_name

    def add_durable(self):
        self.durable = self.durable + 10
        return self.durable

    def update_info(self):
        new_durable = self.durable
        return new_durable





#显示日期和时间
def showtime():
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

mypig = Pig('小猪',12)

# 这是做的第一个宠物!
def pigdosomthing_loop():
    while True:
        pigact = random.randint(0,4)
        if pigact == 1:
            mypig.sit()
            time.sleep(3)
        elif pigact == 2:
            mypig.eat()
            time.sleep(3)

def pigdo():
    pigact = random.randint(0,4)
    if pigact == 1:
        mypig.sit()
    elif pigact == 2:
        mypig.eat()

#开宝箱完成!
def lootbox():
    for i in range(random.randint(0,4)):
        inlist = str(my_sowrd.display_name())
        random_lootbox.append(inlist)

    print('你打开了一个宝箱')
    print('.......................')
    for i in random_lootbox:
        print(i)


showtime()
pigdo()


#实验从list中读取数据并输入给Item的子类,产生独特的输出,同事修改了一次耐久
my_sowrd = Great_sword(*item_list_swords[0])#用*list把list展开!
print(my_sowrd.onename())#显示独特名称
my_sowrd.add_durable()#修改耐久
print(my_sowrd.update_info())





#lootbox()






