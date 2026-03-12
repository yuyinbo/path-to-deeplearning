# 作者: 余殷博
# cangj87@gmail.com


num_list = []
for i in range(10):
    num_list.append(i)
print(num_list)

# 或者使用列表生成式
num_list1 = [i for i in range(10)]
print(num_list1)

# 两层for

# 一维
num_list2 = [j for i in range(5) for j in range(i)]
print(num_list2)
# 等价于
# num_list2 = []
# for i in range(5):
#     for j in range(i):
#         num_list2.append(j)

# 二维
num_list3 = [[i * j for i in range(5)] for j in range(5)]
print(num_list3)
# 等价于
# num_list3 = []
# for j in range(5):
#     inner = []
#     for i in range(5):
#         inner.append(i*j)
#     num_list3.append(inner)

num_list4 = [i for j in num_list3 for i in j]
print(num_list4)

# 使用if只生成奇数
num_list5 = [x for x in range(10) if x % 2 == 1]
print(num_list5)
# 等价于
# result = []
# for x in range(10):
#     if x % 2 == 1:
#         result.append(x)

# if-else三元表达式，实际上两种if并不是同一种
num_list6 = [x if x % 2 == 1 else x ** 2 for x in range(10)]
# 如果是奇数则添加x，如果是偶数则添加x^2
print(num_list6)
# 等价于
# result = []
# for x in range(10):
#     if x % 2 == 1:
#         result.append(x)
#     else:
#         result.append(x**2)
