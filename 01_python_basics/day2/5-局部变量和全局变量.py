# 作者: 余殷博
# cangj87@gmail.com

num = 100  # num是一个全局变量，所有函数都可以使用


def demo1():
    print(num)


def demo2():
    # print(num) 预解析认为是局部变量，没找到
    num = 50  # 实际上定义了一个新的局部变量
    print(num)


def demo3():
    global num  # 如果要在函数内修改全局变量，必须从外面借用全局变量
    print(num)
    num = 25
    print(num)


demo1()
print('-'*50)
demo2()
print(num)
print('-'*50)
demo3()
print(num)
