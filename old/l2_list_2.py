# -- coding: utf-8 --
# 学习list第二天
#import sys

#下面是很好用的字颜色列表
def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

#print_format_table()

alist=['武当派','少林派','甘草派','火神派','经方派']
for pai in alist[-2:]: #遍历整个list,后面[]里面是切片,就是一个范围内,-2是倒数如果是[:]就是拷贝整个列表
    print(pai+"都不错啊")

blist=('武当派','少林派','甘草派','火神派','经方派')#整个()里面是不能修改的列表
for pai in blist:
    print('\x1b[1;37;42m' + pai + '\x1b[0m')


for value in range(1,9,3):#range是从1开始到9,然后每一次加3
    print(value)
