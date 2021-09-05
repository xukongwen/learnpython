# -- coding: utf-8 --
#这里学习list
a= 123
alist=[a,"你好",123]
print(alist[1])#取第二个,从0开始,所以是1
print(alist[-1])#-1就是列表最后一个
blist=["武当派","太极","无门派","经方派","火神派"]
print("我当然是"+blist[3])
blist[0]='张仲景'# 这是改变列表中的值
print("我当然最爱"+blist[0])
print("一共%d个门派"%len(blist))#len()就是计算列表长度

#append是像列表最后加入一个值
blist.append('甘草派')
print("那么我还是"+blist[-1])#证明是在最后

#创建空列表,然后可以动态添加,下面是输入添加
clist=[]
clist.append(input("加入1"))
clist.append(input("加入2"))
print(clist)

#insert是在这个值的位置前面插入
clist.insert(1,input("插入到中间"))
print(clist)

#del是直接把这个值彻底删除,以后不能再用
del clist[1]
print(clist)

#pop就是移除,但还保留值
poped_clist=clist.pop(0)
print(clist)
print(poped_clist)

#remove是不知道位置在哪里,但知道值是什么,也会记录下来
dlist=[1,2,3]
dlist.remove(2)
print(dlist)
