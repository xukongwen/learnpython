# -- coding: utf-8 --
#学习python的文字游戏

#拥有的所有药材和数量
allyao={
    '炙甘草':100,
    '干姜':100,
    '附子':100,
    '大枣':100,
    '桂枝':100,
    '芍药':100,

    }
#分别方剂的配方
sinitang_0={
    '炙甘草':30,
    '干姜':20,
    '附子':10,
    }
guizhitang_0={
    '桂枝':50,
    '炙甘草':40,
    '干姜':30,
    '芍药':10,
    '大枣':10,
    }
#所有的方剂
allfang={
    '四逆汤':sinitang_0,
    '桂枝汤':guizhitang_0,
    }
#帮助提示,所有可用命令
commands = {
                "i" : "打开药箱",
                "c" : "查看张仲景的经方",
                "查看 经方名称" : "查询经方组成",
                "制作 方名" : "从药箱内按方抓药",
           }

print('可输入"帮助"')

n = 0






#游戏主体开始
while True:#最常用的命令输入循环
#下面这一段是非常重要的,对于一个文字输入游戏来说,
#可以判断输入的命令和命令的对象!(深挖的话可以制作出类似dos那种系统)
    command = input('输入>').split()#这个是个逆天神技,其实主要是将输入分组了,后面可以直接调用组内的命令

    if len(command) == 0:
        continue
    if len(command) > 0:
        verb = command[0]#已经给command分组了,所以就可以给command赋予任何命令
    if len(command) > 1:
        item = command[1]#已经分组
#查看帮助
    if verb == '帮助':
        print('\n')
        print('游戏内有如下命令:\n')
        for key in commands:#这里有一个知识点,就是放一个变量在in字典前,就自动是找到该字典的key
            print('\t',key+':'+str(commands[key]))
        print('\n')
#查看药箱内的药物存量
    elif verb == 'i':
        print('\n')
        print('你的药箱内有:\n')
        for key in allyao:
            print('\t',key+':'+str(allyao[key]))
        print('\n')
#打印已经学会的经方
    elif verb == 'c':
        print('\n')
        print('你学会有如下经方:\n')
        for key in allfang:
            print('\t',key)
        print('\n')
#下面是在字典中查询并打印出查询结果
    elif verb == '查看':
        print('\n')
        if item in allfang:#整个 if 某某某 in很有用,就是判断某某某是否在字典里,或list里或任何里
            print('%s的组成为:\n'%item)
            for yao, yaoliang in allfang[item].items():
                print('\t',yao,yaoliang)

    elif verb == '制作':
        print('\n')
        if item in allfang:
            print('你需要如下:\n')
            for yao, yaoliang in allfang[item].items():
                print('\t需要:'+str(yao)+str(yaoliang))
                print('\t你有:'+str(yao)+str(allyao[yao]))
            print('\n')

            canBeMade = True

            for yao in allfang[item]:
                if allfang[item][yao] > allyao[yao]:#库存要足够
                    print('药材不足,无法制作')
                    canBeMade = False
                    break

            if canBeMade == True:
                for yao in allfang[item]:
                    allyao[yao] -= allfang[item][yao]#从背包里减去制作需要的
                    if allyao[yao] <= 0:#判断如果没有了,就直接从背包里删除掉
                        del allyao[yao]
                        #print('删除')

                allyao[item] = n+1



                print('制作成功')
