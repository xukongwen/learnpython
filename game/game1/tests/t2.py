#今天这里学的太多,而且非常重要!是面对对象编程的一个很好的例子!正确编程思维最重要!


#如何动态创建实例?


class Loot_box():
    def __init__(self,player):
        self.player = player
        pass

    def exchange(self):
        a = [1]
        self.player.add_inv(a)
        


class Player():
    def __init__(self):
        self.inv = []
        pass

    def add_inv(self,item):
        self.inv.append(item)
        pass

    def remove_inv(self,item):
        self.inv.remove(item)
        pass
       
    def show(self):
        print(self.inv)
       
        

class Show():
    def __init__(self):
        self.flag = True
        self.run = False
        pass
    
    def show(self):
        if self.run == True and self.flag:
            self.flag = False
            #print(self.run)
            print('hi')
        else:
            pass
            



l1 = [['桂枝汤','甘草','大枣','干姜','桂枝','芍药'],['四逆汤','甘草','附子','干姜']]

l2 = ['甘草','干姜','附子']
l3 = ['附子','甘草']
l4 = ['附子']

final_list = []

def craft1():
    #切掉名字,剩下方子
    for i in l1:
        list1 = i[1:]
        final_list.append(list1)


    n= 0
    for a in final_list:
        if len(l2) == len(a):
            for i in l2:
                for j in a:
                    if i in j:
                        n += 1

    if n == 0:
        print('不在经方中')
    else:

        if n == len(l2):
            print('满足制作要求')
        else:
            print('材料不够')

#craft1()

f1 =[['四逆汤',['甘草',30],['干姜',20],['附子',10]],['桂枝汤',['甘草',30],['干姜',20],['芍药',10],['大枣',50],['桂枝',40]]]
p1 = [['甘草',30],['干姜',20],['附子',10]]
p2 = [['附子',30],['干姜',20],['甘草',5]]
p3 = [['附子',3],['干姜',2],['甘草',30]]

fang = []

def craft2(player):
    n=0
    for i in f1:
        list2 = i[1:]
        fang.append(list2)

    mm = 0
    lack = 'hi'
    lack_list = []

    for a in fang:
        if len(player) == len(a):
            for i in player:
                for j in a:
                    if i[0] in j[0]:
                        #print('player:',i[0],i[1],"fang:",j[0],j[1])
                        if i[1] == j[1]:
                            n += 1
                        elif i[1] < j[1]:
                                mm = j[1] - i[1]
                                lack = i[0]
                                lack_list.append(lack)

    if n == 0:
        print('no')
    else:
        if n == len(player):
            print('满足制作要求')
        else:
            for q in lack_list:
                print(q,'缺少',mm)
            
    

   

craft2(p1)

craft2(p3)
    


          
           
    
    







    