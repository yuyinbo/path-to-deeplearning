# 作者: 余殷博
# 如果断言表达式是假则会抛异常

def input_password():
    """
    自定义异常并抛出
    :return:
    """
    password = input('请输入密码:')
    assert len(password) >= 8, '密码长度应不小于8'
    # 如果后面的表达式为假，则会抛出AssertionError并显示之后的内容
    return password


try:
    pwd = input_password()
    print(pwd)
except Exception as e:
    print("错误", e)
