# 作者: 余殷博
# cangj87@gmail.com
a = (1, 2, 3)
b = ('a', 'b', 'c')

print(list(zip(a, b)))  # 将两个可迭代对象的元素依次配队（多余的则删掉）
print(dict(zip(a, b)))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

for index, val in enumerate(seasons):
    print(index, val)
# 遍历可迭代对象时，同时得到索引和元素（返回的是一个可迭代对象）
my_dict = {val: index for index, val in enumerate(seasons)}
print(my_dict)
my_dict = {index: val for index, val in enumerate(seasons)}
print(my_dict)
# 字典生成式
