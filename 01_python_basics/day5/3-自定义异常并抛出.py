# 作者: 余殷博
# cangj87@gmail.com


def input_password():
    """
    自定义异常并抛出
    :return:
    """
    password = input('请输入密码:')
    if len(password) >= 8:
        return password
    raise Exception('密码长度应不小于8')
    # 自定义一个异常，如果密码长度小于八位会主动抛出
    # 实际上只是创建了Exception类里的一个对象


try:
    pwd = input_password()
    print(pwd)
except Exception as e:
    print("错误", e)
