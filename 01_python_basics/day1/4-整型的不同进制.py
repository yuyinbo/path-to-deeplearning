# 作者: 余殷博
# cangj87@gmail.com

# 整型是无穷大的（初始分配28字节），不会溢出
a = 123
print(a)
# 转换成二进制，结果是一个字符串，以下的转换只是为了显示
print(bin(a))
print(type(bin(a)))
# 转换成十六进制
print(hex(a))
# 转换为八进制
print(oct(a))

# 补码（8位）
# 5 0b 0000 0101
# -5 08b 1111 1011
