# 作者: 余殷博
# cangj87@gmail.com

# 参数个数不确定的函数

def demo(num, num1, *args, **kwargs):
    """
    单个参数，元组，键值对(字典）
    args和kwargs可以为空
    :param num1:
    :param num:
    :param args:
    :param kwargs:
    :return:
    """
    print(num)
    print(num1)
    print(args)  # arguments 位置参数
    print(kwargs)  # keyword arguments 关键字参数


demo(1, 2, 3, 4, name='Steve', age=18)
print()
demo(1, 2, name='Miko', title='Queen')
print()
print()


# 位置参数只取位置上的参数，形如“x=y"的都是关键字参数，放在字典里

def demo1(num, num1, *args, **kwargs):
    """
    传递位置参数和关键字参数
    :param num1:
    :param num:
    :param args:
    :param kwargs:
    :return:
    """
    demo(num, num1, args, kwargs)
    # 将元组args，字典kwargs整体作为元组传递了
    print()
    demo(num, num1, *args, **kwargs)
    # 要使用拆包，使*args = *args，其中字典用**拆包


demo1(1, 2, 3, 4, name='Miko', age=16)
