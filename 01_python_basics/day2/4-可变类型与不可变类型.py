# 作者: 余殷博
# cangj87@gmail.com

# 整型是不可变类型（内存中的数据不允许被修改，只能修改变量的指向）
def change(num):
    """
    通过传参无法改变数据本身
    :param num:
    :return:
    """
    print(f'num={num}, id(num)={id(num)}')
    num = 5  # num挂在5上面去了
    print(f'修改后 num={num}, id(num)={id(num)}')


def list_change(lst):
    """
    可变类型通过传参可以修改数据本身，而不改变引用
    :param lst:
    :return:
    """
    lst[0] = 7
    print(f'函数内lst={lst}, id(lst)={id(lst)}')


a = 10
print(f'id(a)={id(a)}')
change(a)  # a和num挂在一起
print(f'函数外 a={a}')

print('-' * 50)

# 列表是可变类型
my_list = [1, 2, 3]
print(f'id(my_list)={id(my_list)}, my_list={my_list}')
my_list[0] = 5  # 修改了数据而没有修改引用
print(f'id(my_list)={id(my_list)}, my_list={my_list}')

print('-'*50)

list_change(my_list)
print(f'函数外my_list={my_list}, id(my_list)={id(my_list)}')