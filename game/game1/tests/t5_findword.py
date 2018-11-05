#正则表达式学习结合pandas以及matplotlib画图

import re
import sys
import pandas as pd
import matplotlib as mpl
import  matplotlib.pyplot as plt
import numpy as np
import pygal
from matplotlib.font_manager import FontManager
from pylab import mpl
import subprocess

plt.rcParams['font.sans-serif']=['STSong'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


p1 = '如是'
p2 ='我'
p3 = '幻'
p4 = '佛'
p5 = '眾生'


w_list = [p1,p2,p3,p4,p5,'無','空']
shanghan1 =['桂枝湯','四逆湯','湯','桂枝','發汗','悪寒','吐','死','傷寒','熱','寒','下利']


class Find_word():
    def __init__(self,w_list,w_file):
        self.file = w_file
        with open(self.file) as f:
            self.data = f.readlines()
        self.list = w_list
        self.s_list = []
        

    def count(self,p):
        self.x = []
        self.a = []
        self.p = p
        self.n = 0

        for line in self.data:
                self.x = re.findall(self.p,line)
                if self.p in self.x:
                    self.a.append(self.x)

        for i in self.a:
            if self.p in i:
                for j in i:
                     if self.p in j:
                        self.n += 1
        return self.n
        

    def show(self):
        plt.xlabel('目标词汇词')
        plt.title('PHANTOM数据分析')

        for i in self.list:
            self.s_list.append(self.count(i))
            plt.text(i,self.count(i)+3,self.count(i))

        plt.bar(self.list,self.s_list)
        plt.show()




pp = Find_word(shanghan1,'shanghan.txt')

pp.show()
    












