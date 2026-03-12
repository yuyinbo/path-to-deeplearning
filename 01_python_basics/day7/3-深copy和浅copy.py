# 作者: 余殷博
# cangj87@gmail.com
import copy

a = [12, 22]
b = [33, 44]
c = a
print(c)
a[0] = 50
print(c)
# 直接赋值，a和c指向同一块内存块，修改a会改变c的值
print()

a = [12, 22]
c = copy.copy(a)
# 主要用于复制自定义对象，这是浅拷贝
print(c)
a[0] = 50
print(c)
print()

a = [12, 22]
c = [a, b]
d = copy.copy(c)
# d=c.copy() 列表的copy方法是浅拷贝
print(d)
a[0] = 50
print(d)
print(f'id(c)={id(c)}, id(d)={id(d)}')
# c和d的id不同，但是里面的内容相同，即指向的内存块相同
print(f'id(c[0])={id(c[0])}, id(d[0])={id(d[0])}')
# 浅拷贝只会创建外层容器对象的副本，内层元素还是原来的引用
print()

a = [12, 22]
c = [a, b]
d = copy.deepcopy(c)
# 深拷贝
print(d)
a[0] = 50
print(d)
print(f'id(c)={id(c)}, id(d)={id(d)}')
print(f'id(c[0])={id(c[0])}, id(d[0])={id(d[0])}')
# 深拷贝是递归拷贝对象的所有层次，直到不可变数据类型，创建一个完全独立的副本
print('-'*50)

