# 作者: 余殷博
# cangj87@gmail.com
import os


def open_rb():
    """
    以二进制模式打开，读出的是字节流
    字节流不可以加入 'encoding=' 参数
    :return:
    """
    file = open('Hong_Kong.jpg', 'rb')
    print(file.read(100))
    file.seek(0)
    file1 = open('Hong_Kong[副本].jpg', 'wb')
    file1.write(file.read())
    file.close()
    file1.close()


def use_seek():
    """
    改变位置指针
    :return:
    """
    file = open('file1', 'r+', encoding='utf8')
    file.seek(5, os.SEEK_SET)
    # 位置指针，相对文件开头向后移动五个字节
    # os.SEEK_SET指文件开头，或者写参数0
    # os.SEEK_CUR指当前位置，或者写参数1
    # os.SEEK_END指文件结尾，或者写参数2
    # 相对文件结尾时，如果不是二进制模式，偏移量只能写0
    txt = file.read()
    print(txt)


def use_seek1():
    """
    改变位置指针
    :return:
    """
    file = open('file1', 'rb+')
    file.seek(-6, os.SEEK_END)
    # 如果是二进制模式，可以倒数的字符
    txt = file.read()
    print(txt)


def use_seek_wp():
    """
    seek和w+的使用
    :return:
    """
    file = open('file0', 'w+', encoding='utf8')
    file.write('how are you')
    file.seek(0, os.SEEK_SET)  # 光标回到开头
    txt = file.read()
    print(txt)
    file.close()


if __name__ == '__main__':
    open_rb()
    use_seek()
    # 位置指针先移动到Hello之后，读到的是" World..."
    use_seek1()
    use_seek_wp()
