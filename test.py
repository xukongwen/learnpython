
def test_bag_jian ():

    score = 3
    class_list = {'apple':30}
    while True:
        name = input()

        score = score-1

        print('a', repr(class_list))

        if score <= 0:
            del class_list[name]
            print('del')
        else:
            class_list[name] = score


        print(class_list)


def test_bag_add ():

    score = 0
    class_list = {'apple':30}
    while True:
        name = input()

        score = score + 1

        class_list[name] = score

        print(class_list)

test_bag_add()
