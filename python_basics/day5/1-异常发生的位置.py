# 作者: 余殷博
# cangj87@gmail.com

def print_exception_pos(e):
    """
    打印异常位置
    :param e:
    :return:
    """
    print(e)
    print(e.__traceback__.tb_frame.f_globals['__file__'])
    # 发生异常的文件
    # e
    # 异常对象
    # ↓
    # __traceback__
    # 异常的调用栈
    # ↓
    # tb_frame
    # 发生异常的栈帧
    # ↓
    # f_globals
    # 该模块的全局变量
    # ↓
    # ['__file__']
    # 这个模块的文件名
    print(e.__traceback__.tb_lineno)
    # 发生异常的行数


try:
    a = 1 / 0
except Exception as e:
    print_exception_pos(e)
