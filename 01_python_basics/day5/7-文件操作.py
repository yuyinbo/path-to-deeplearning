# 作者: 余殷博
# cangj87@gmail.com
import os


def use_open_r():
    file = open('file1', 'r', encoding='utf8')
    # Windows默认的汉字编码是GBK而不是UTF-8
    # r代表只读方式，文件的指针将会放在文件的开头，这是默认模式。
    # 如果文件不存在，抛出异常
    txt = file.read()
    print(txt)
    # file.write('今天天气很好')
    file.close()


def use_open_rp():
    """
    使用r+方式打开
    :return:
    """
    file = open('file1', 'r+', encoding='utf8')
    # r+代表读写方式，文件的指针将会放在文件的开头。如果文件不存在，抛出异常
    # write会直接从当前指针处开始覆盖写入
    file.read()
    # 读完之后指针会移到末尾
    num = file.write('\n今天天气很好')
    # write()返回的是写入的字节数
    file.seek(0)
    # 使文件指针移动回开头
    print(file.read())
    file.close()


def use_open_a():
    """
    使用追加方式打开
    :return:
    """
    file = open('file1', 'a', encoding='utf8')
    # 指针起初就会在末尾
    nums = file.write('\nHELLO')
    print(nums)
    file.close()


def use_open_w():
    """
    文件不存在时会创建，如果已经创建就会被清空
    :return:
    """
    file = open('./dir1/dir2/file4', 'w', encoding='utf8')
    # .代表当前路径，'./dir1/file2'构成相对路径、
    # 也可以写成 'dir1/file2'
    # /在windows可以写成\\（因为转义字符）
    # 绝对路径，在Windows形如D:/dir1/...
    # 在Linux形如/dir1/...
    file.close()


def use_readline():
    """
    每次读一行
    :return:
    """
    file = open('file1', 'r+', encoding='utf8')
    while True:
        txt = file.readline()
        # 每行的结尾本来就有一个换行
        if not txt:
            # 读全部行
            break
        print(txt)
        # print默认会再打一个换行


if __name__ == '__main__':
    # use_open_r()
    # use_open_rp()
    # use_open_a()
    use_open_w()
    print(os.getcwd())
    # 查看当前进程的绝对路径
    use_readline()