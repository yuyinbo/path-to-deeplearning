# 作者: 余殷博
# cangj87@gmail.com
import sys
sys.setrecursionlimit(10001)

def f(n):
    """
    从1到n求和
    :param n:
    :return:
    """
    if n == 1:  # 结束条件要写在return语句之前
        return 1
    return n + f(n - 1)


print(f(10000))


def step(n):
    """
    一次可以走一级或者两级，求n级台阶一共有多少种走法
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return step(n-1)+step(n-2)


print(step(5))
