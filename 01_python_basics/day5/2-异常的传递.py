# 作者: 余殷博
# cangj87@gmail.com
import traceback


def demo1():
    n = int(input("请输入一个整数："))
    print(f'demo1, {n}')
    return n


def demo2():
    n = demo1()
    print(f'demo2, {n}')
    return n


try:
    num = demo2()
    # 如果发生了异常，后面都不会执行
    print(f'main, {num}')
except Exception as e:
    print(e)
    traceback.print_exc()
    # 查看traceback
    # traceback最下面是异常类型，倒数第一个位置是真正出错的地方
    # 再往上是调用链
