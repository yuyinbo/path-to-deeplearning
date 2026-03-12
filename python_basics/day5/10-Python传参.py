# 作者: 余殷博
# cangj87@gmail.com

import sys

print(sys.argv)


# argv是一个列表，内容是运行Python程序时在CMD输入的参数


def use_argv():
    """
    根据传递的参数不同，打开不同的文件，读取内容并打印
    :return:
    """
    file = open(sys.argv[1], 'r+', encoding='utf8')
    # argv[0]是本脚本
    print(file.read())
    file.close()


use_argv()
