# -- coding: utf-8 --
# 练习用
from sys import argv
from os.path import exists

print("hi")
#我的名字 = '徐空文'
#我的年龄 = 400
#下面这个很有用，估计以后做简单的输入输出的时候需要这个
#print("我叫：%s，我的年龄是：%s"%(我的名字,我的年龄))
#这个%r就是全部引用的感觉
#print("%r"%我的名字)
# 伟大的写诗模式
#print("""
#这就是传说中的写诗模式吗？
#    那么真的吗？
#    是的吗？
#可以吗？
#"""
#)
#这个也比较常用
#
#print("你叫啥？")
#age=input()#这里就是输入了！
#print("你叫：%s"%age)

#who=input("你到底是谁？")
#print("错，你不是%s!"%who)

#这里是运行文件的后缀
#scname = argv#这个argv就是运行文件后面写的东西
tishifu = '输入：>'

print("输入要写入的文件名：")
newfile=input(tishifu)
newtext=open(newfile, 'w')#这里必须有’w'这个东西，就是可以读和写入
print("\n")


print("现在要写入一些东西：")
line1=input(tishifu)
line2=input(tishifu)

newtext.write(line1)
newtext.write("\n")
newtext.write(line2)

print("写入完毕！")
newtext.close()
newtext=open(newfile)#为了下面读取，需要再打开一遍
data=newtext.read()#貌似每一次read都要再打开一次我曹！

print("输入将要拷贝的文件名：")
copyname=input(tishifu)
copyname_data=open(copyname, 'w')
copyname_data.write(data)
copyname_data.close()
newtext.close()
print("拷贝完毕！")
print("验证文件内容：\n", data)
