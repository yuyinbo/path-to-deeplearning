# 作者: 余殷博
# cangj87@gmail.com


print(eval('1+1'))


# eval()的内容是将字符串内的内容当作代码执行

def read_conf():
    """
    读取配置
    :return:
    """
    file = open('config', 'r', encoding='utf8')
    txt = file.read()
    print(txt)
    print(type(txt))
    # 直接读取文件得到的是字符串
    conf_dict = eval(txt)
    print(conf_dict)
    print(type(conf_dict))
    file.close()


if __name__ == '__main__':
    read_conf()
