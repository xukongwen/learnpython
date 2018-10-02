# -- coding: utf-8 --
# 学习list第三天
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

#最基本的字典
sinitang_0={
    #'name':'四逆汤',
    'pill_1':['甘草',30],
    'pill_2':['干姜',20],
    'pill_3':['附子',10]
    }
#print('%s的组成:'%sinitang_0['name'])

for key,value in sinitang_0.items():#.items()是取出{}里的key以及value
    print ("key is:",key)
    print('value is:',value)

for name in sinitang_0.keys():#.keys()只取出key
    print('key:',name)

for value in sinitang_0.values(): #.values()只取出values,set()是读取独一无二的,可是对list无效
    for list in value:
        print(sinitang_0[list][1])
