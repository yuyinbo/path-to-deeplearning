# 作者: 余殷博
# cangj87@gmail.com
import os


def use_rename():
    os.rename('dir1/file3.txt', 'dir1/file4.txt')


def use_remove():
    """
    只能删除普通文件（不是目录的文件）
    :return:
    """
    os.remove('dir1/file4.txt')


def use_listdir():
    print(os.listdir('.'))
    # .代表当前目录
    print(os.listdir('..'))
    # ..代表上一级目录
    print(os.listdir('../..'))
    # ../..代表上一级目录的上一级目录


def use_chdir():
    """
    改变当前进程的工作路径
    目的是为了减少相对路径长度
    :return:
    """
    print(os.getcwd())
    # 获取当前工作目录
    os.chdir('..')
    # 改变当前工作目录（到上一级目录）
    print(os.getcwd())


def scan_dir(path, width):
    """
    深度优先遍历目录
    使用isdir()
    :param width:
    :param path:
    :return:
    """
    file_names = os.listdir(path)
    # 本目录下所有的文件
    for file_name in file_names:
        print(" " * width + file_name)  # 打印名字
        new_path = path + '/' + file_name
        # 如果是文件夹，必须拼接路径，否则进不去
        if os.path.isdir(new_path):
            # 如果file_name是一个文件夹
            scan_dir(new_path, width + 2)


def use_stat():
    """
    获取文件的信息
    :return:
    """
    file_info = os.stat('file1')
    print('size{},uid{},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                        file_info.st_mtime))
    from time import strftime
    from time import gmtime
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime(file_info.st_mtime)))


if __name__ == '__main__':
    file = open('./dir1/file3.txt', 'w', encoding='utf8')
    file.close()
    use_rename()
    use_remove()
    # 创建重命名并删掉
    use_listdir()
    use_chdir()
    scan_dir('.', 0)
    os.chdir('day5')
    use_stat()
