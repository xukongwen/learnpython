
commands = {
                "i" : "打开药箱",
                "c" : "查看张仲景的经方",
                "craft [item]" : "从药箱内按方抓药",
           }

#an inventory of items
items = {
            "flint" : 50,

            "grass" : 100,
            "hay" : 0,

            "tree" : 100,
            "log" : 0,

            "sapling" : 100,
            "twig" : 0,

            "boulder" : 30,
            "rock" : 0,

            "pickaxe" : 0,
            "axe" : 0,

            "firepit" : 0,
            "tent" : 0,

            "torch" : 0,
        }

#rules to make new objects
craft = {
            "hay" : { "grass" : 1 },
            "twig" : { "sapling" : 1 },
            "log" : { "axe" : 1, "tree" : 1 },
            "axe" : { "twig" : 3, "flint" : 1 },
            "tent" : { "twig" : 10, "hay" : 15 },
            "firepit" : { "boulder" : 5, "log" : 3, "twig" : 1, "torch" : 1 },
            "torch" : { "flint" : 1, "grass" : 1, "twig" : 1 },
            "pickaxe" : { "flint" : 2, "twig" : 1 }
        }


print("'Crafting Challenge' Game")
print("More programs at UsingPython.com/programs")
print("-----------------------------------------\n")


print("TRY TO SURVIVE BY CRAFTING A TENT AND A FIREPIT!")
print("type '?' for help")

while True:
# 这里是进行输入命令的拆分
    command = input(">").split()

    if len(command) == 0:
        continue
#下面是判断命令和输入的命令,大于0的那个是命令,大于1的是命令的对象
    if len(command) > 0:
        verb = command[0].lower()
    if len(command) > 1:
        item = command[1].lower()

    if verb == "?":
        for key in commands:
            print(key + " : " + commands[key])#找到并输出这一行的命令
        print("\n")

    elif verb == "i":
        for key in items:
            print(key + " : " + str(items[key]))
        print("\n")

    elif verb == "c":
        for key in craft:
            print(key + " can be made with:")

            for i in craft[key]:
                print(str(craft[key][i]) + " " + i)

            print("\n")

    elif verb == "craft":

        print("making " + item + ":")
        if item in craft:

            for i in craft[item]:
                print("  you need : " + str(craft[item][i]) + " " + i + " and you have " + str(items[i]))

            canBeMade = True

            for i in craft[item]:
                if craft[item][i] > items[i]:
                    print("item cannot be crafted\n")
                    canBeMade = False
                    break

            if canBeMade == True:
                for i in craft[item]:
                    items[i] -= craft[item][i]

                items[item] += 1

                print("item crafted\n")


            if items["tent"] >= 1 and items["firepit"] >= 1:
                print("\n**YOU HAVE MANAGED TO SURVIVE!\nWELL DONE!")
                break

        else:
            print("you can't")

    else:
        print("you can't")
