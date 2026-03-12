# 作者: 余殷博
# cangj87@gmail.com
import random


def use_if():
    # 1. 定义年龄变量
    age = 18
    # 2. 判断是否满 18 岁
    # if 语句以及缩进部分的代码是一个完整的代码块
    if age >= 18:
        print("可以进网吧")
    else:
        print("不能进")
    # 3. 无论条件是否满足都会执行
    print("这句代码什么时候都会执行")


def use_elif():
    holiday_name = "平安夜"
    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日啊……")


def use_random():
    a = random.randint(1, 3)  # 调用random生成随机数
    b = input("石头剪刀布：")
    b = int(b)
    if a == b:
        print("平局")
    elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
        print("computer=%d，你输了" % a)
    else:
        print("computer=%d，你赢了" % a)


use_if()
use_elif()
use_random()
