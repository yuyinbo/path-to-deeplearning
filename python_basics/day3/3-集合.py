# 作者: 余殷博
# cangj87@gmail.com

my_set = {}
# 得到的是空字典而不是空集合
print(my_set)
print(type(my_set))

my_set = set()
# 这样才是空集合
print(my_set)
print(type(my_set))

my_set = {"apple", "banana", "cherry"}
print('apple' in my_set)
# 是否在集合中

lst = [1, 1, 1, 2, 3]
print(set(lst))
# 集合用于去重

a = [1, 2, 3]
b = a.copy()
# 返回一个内容相同但地址不同的对象，直接赋值则会挂在相同内容上
print(f'id(a)={id(a)}, id(b)={id(b)}')
a[0] = 5
print(a)
print(b)

set1 = {1, 2, 3}
set2 = set1.copy()
# 同样返回内容相同的新集合
print(id(set1))
print(id(set2))

# 运算符重载
a = set('abcdefg')
b = set('abch')
print(a, b)
print(a - b)  # difference
print(a | b)  # union
print(a & b)  # intersection
print(a ^ b)  # union-intersection，(A−B)∪(B−A)，即只出现一次的元素
