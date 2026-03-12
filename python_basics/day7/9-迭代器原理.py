# 作者: 余殷博
# cangj87@gmail.com

for i in range(10):
    print(i, end=' ')

# 自定义一个类似range(n)的对象

print()


def f(n):
    """
    含有yield的函数被称为生成器函数
    本质上是一种特殊的迭代器
    迭代器本身是定义了"__iter__"和"__next__"的一个类
    :param n:
    :return:
    """
    t = 0
    while t < n:
        yield t
        # yield作用是暂停函数，保存状态，下次迭代时从下一句开始执行
        # yield t表示将t返回给调用者，并保存当前状态
        t += 1
    return


for i in f(10):
    print(i, end=' ')
    # 执行的过程是：开始，遇到yield 1, 给i返回1，保存状态，暂停函数
    # 下一次迭代时，从yield 1的下一句开始执行，返回2，保存状态，暂停函数
    # 执行直到结束或遇到return，如果没有更多yield，抛出异常StopIteration，被for捕获，循环结束
print()

my_iter = f(2)
# 创建迭代器对象
print(next(my_iter))
# 返回0
print(next(my_iter))
# 返回1
try:
    print(next(my_iter))
except StopIteration:
    print("迭代结束")
# 抛出异常StopIteration
print('-' * 50)
my_iter = f(3)
for i in my_iter:
    print(i)
for i in my_iter:
    print(i)
# 迭代器如果没有在__iter__里创建一个新迭代器对象，只能被遍历一次，此生成器函数就是这样的
print()
my_list = [1, 2, 3]
for i in my_list:
    print(i)
for i in my_list:
    print(i)
# 列表不是迭代器，而是可迭代对象，可以反复遍历
# 这是因为每次for循环开始时，都调用了__iter__方法，返回一个新的迭代器对象
