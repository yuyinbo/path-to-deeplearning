# 作者: 余殷博
# cangj87@gmail.com

def use_len_count():
    name_list = ['张三', '李四', '王五', '王小二', '张三']

    print(len(name_list))  # 容器中的元素总数

    print(name_list.count('张三'))  # 某元素出现次数

    name_list.remove('张三')  # 删除第一次出现的
    print(name_list)


def use_sort():
    """
    使用排序
    :return:
    """
    name_list = ['zhangsan', 'lisi', 'wangwu']
    num_list = [6, 8, 5, 1, 10]

    print(name_list, '\n', f'id(name_list) = {id(name_list)}')
    print(num_list, '\n', f'id(num_list) = {id(num_list)}')
    # 只有列表元素类型均相同时才能排序
    name_list.sort()  # 按首字母ASCII
    num_list.sort()  # 按数字大小

    print(name_list, '\n', f'id(name_list) = {id(name_list)}')
    print(num_list, '\n', f'id(num_list) = {id(num_list)}')
    num_list.sort(reverse=True)  # 倒序
    print(num_list)


def use_reverse():
    name_list = ["zhangsan", "lisi", "wangwu"]
    num_list = [6, 8, 4, 1, 10]
    # 逆序（反转）
    name_list.reverse()
    num_list.reverse()
    print(name_list)
    print(num_list)


def use_iter():
    """
    遍历
    :return:
    """
    name_list = ["zhangsan", "lisi", "wangwu", "zhangsan", "zhangsan"]
    for name in name_list:
        print(name, end=' ')
    print()
    i = 0
    while i < len(name_list):
        print(name_list[i], end=' ')
        i += 1
    print()  # 两种遍历的方式

    i = 0
    n = name_list.count('zhangsan')
    while i < n:  # 删除所有zhangsan，应使用while而不是for
        name_list.remove('zhangsan')
        i += 1
    print(name_list)
    print()


use_len_count()
print('-' * 50)
use_sort()
print('-' * 50)
use_reverse()
print('-' * 50)
use_iter()
