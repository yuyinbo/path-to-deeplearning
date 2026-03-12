# 作者: 余殷博
# cangj87@gmail.com

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # 两个列表值是相同的
print(id(a) == id(b))
print(a is b)
# 上述两行是等价的
a = b
print(a is b)
# 当b赋值给a, 则a和b都指向相同对象了
