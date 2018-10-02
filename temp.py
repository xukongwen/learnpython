sinitang_0={
    '炙甘草':30,
    '干姜':20,
    '附子':10
    }
guizhitang_0={
    '桂枝':50,
    '炙甘草':40,
    '干姜':30,
    '芍药':10,
    '大枣':10
    }

allyao={
    '四逆汤':sinitang_0,
    '桂枝汤':guizhitang_0
    }
#print(sinitang_0['pill_1'][0])
#s=sinitang_0['pill_1'][0]
#b=sinitang_0['pill_1'][1]
#print("用药>%s:%s克"%(s,b))
#print(sinitang_0.values())

#整个思路就不对
def test1():
    yao1=input("输入:>")
    for yao in allyao:
        if yao1 in allyao:
            print("found:")
            print(allyao['四逆汤'])
            break
        else:
            print("not found")
            break
# 我曹!整个是如何在字典里找到对应的东西然后打印出来!非常重要!用的是item()整个命令!
def test2():
    yao1=input("输入:>")
    for name, craft in allyao.items():
        if yao1==name:
            print('这是%s的经方:'%yao1)
            for name, amount in craft.items():
                print(name,amount)

test2()

#test1()
