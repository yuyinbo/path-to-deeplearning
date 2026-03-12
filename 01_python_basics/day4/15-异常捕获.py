# 作者: 余殷博
# cangj87@gmail.com


def use_exception():
    """
    简单的异常捕获
    :return:
    """
    try:
        num = int(input("请输入一个数字："))
        print(num)
    except:
        print('请输入数字而不是其他类型')


def use_exception_type():
    """
    不同的异常类型
    :return:
    """
    try:
        num = int(input("请输入一个整数："))
        print(8 / num)
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('不能除以0')
    except Exception as e:
        print(e)


def use_else_finally():
    try:
        num = int(input("请输入一个整数："))
        print(8 / num)
    except ValueError:
        print('请输入整数')
    except ZeroDivisionError:
        print('不能除以0')
    except Exception as e:
        # 其他所有类型的异常
        print("未知错误%s" % e)
    else:
        # 假如没有异常
        print('正常执行')
    finally:
        # 无论有没有异常都会执行
        # 就算前面有return，或者中途退出也会执行
        print('\n执行结束')


if __name__ == '__main__':
    # use_exception()
    # use_exception_type()
    use_else_finally()
