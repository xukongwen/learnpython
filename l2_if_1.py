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
# 字颜色实例
#print('\x1b[1;37;42m' +'忽然发现,其实五行几乎把所有人的性格也很好概括了' + '\x1b[0m')

#解决昨天没解决的问题
alists = ['男','女','不详']
sex=input('请输入性别:')
if sex in alists:
    print('好的,你是个%s人'%sex)
else:
    print('你在玩我吗?')
    while sex!='男' and sex!='女' and sex!='不详':
        sex=input("再次输入性别:")
    print('好的,我知道你是%s人了'%sex)
