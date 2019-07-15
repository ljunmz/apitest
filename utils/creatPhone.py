import random


def createPhone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


# # 生成手机号
# phone = createPhone()
# print(phone)


def randomPhone():
    list = ['140', '141', '142', '143', '144', '145', '146', '147', '148', '161']
    shou = random.choice(list)
    str = "0123456789"
    haom = ''
    haom1 = []
    for i in range(8):
        haom1.append(random.choice(str))
        haom = ''.join(haom1)
    phone = shou + haom
    print(phone)
    return phone

# randomPhone()
