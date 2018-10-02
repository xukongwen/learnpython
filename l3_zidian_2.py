allyao={
    '炙甘草':100,
    '干姜':100,
    '附子':100,
    '大枣':100,
    '桂枝':200,
    '芍药':100
    }

craftyao={
    '四逆汤':{'炙甘草':30,'干姜':20,'附子':10},
    '桂枝汤':{'桂枝':50,'干姜':30,'炙甘草':40,'芍药':10,'大枣':10}
}



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

allfang={
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
    for yao in allfang:
        if yao1 in allfang:
            print("found:")
            print(allfang['四逆汤'])
            break
        else:
            print("not found")
            break
# 我曹!整个是如何在字典里找到对应的东西然后打印出来!非常重要!用的是item()整个命令!
def test2():
    yao1=input("输入:>")
    for name, craft in allfang.items():
        if yao1==name:
            print('这是%s的方子:'%yao1)
            for name, amount in craft.items():
                print(name,amount)

commands = {
                "i" : "打开药箱",
                "c" : "查看张仲景的经方",
                "craft [item]" : "从药箱内安方抓药",
           }

test2()
