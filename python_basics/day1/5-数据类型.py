# 作者: 余殷博
# cangj87@gmail.com


def use_float():
    """
    查看浮点数精度
    :return:
    """
    f = 1.23456789123456789
    g = 123456789.123456789
    print(f)
    print(g)


def use_bool():
    """
    查看bool类型输出与运算
    :return:
    """
    print(1 == 2)
    print(False + 0)
    # 做运算时化为int


def use_complex():
    """
    使用复数
    :return:
    """
    c = complex(3, 4)
    print('c is %d+%di' % (c.real, c.imag))


def use_char():
    """
    转义字符
    :return:
    """
    print('\'abc\'\n\'edf\'')
    print('abc\\edf')
    print("abc'def'")  # 单引号套双引号或相反不需要\
    print('''' and "''')  # 三引号可以套单引号和双引号而不需要\
    print('abc\rd')  # pycharm结果和cmd不同


def use_ascii():
    """
    使用ASCII
    :return:
    """
    c = 'a'
    print(ord(c))  # 得到c的ASCII
    d = chr(ord(c) - 32)
    print(d)


use_float()
use_bool()
use_complex()
use_char()
use_ascii()
