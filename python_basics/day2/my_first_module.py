# 作者: 余殷博
# cangj87@gmail.com

name = '余殷博'


def print_line(char, nums):
    print(char * nums)
    # print(char1) 这一行在本模块外无法访问char1，就算char1是全局变量


print(__name__)  # 在本模块中是__main__
# 测试本模块
if __name__ == '__main__':  # 以下内容不会在导入该模块时运行
    char1 = '*'
    nums1 = 60  # 是只在本模块内可见的全局变量
    print_line(char1, nums1)
