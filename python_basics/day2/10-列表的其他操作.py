# 作者: 余殷博
# cangj87@gmail.com
a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
c = [0] * 10  # 重复十遍

print(id(a))
print(a * 2)  # 重复两遍
print(c)

a += b  # 等价于a.extend(b)，与a = a + b不同（重新赋值会改变地址）
print(a)
print(id(a))
