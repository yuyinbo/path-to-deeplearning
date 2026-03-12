# 作者: 余殷博
# cangj87@gmail.com
import re

# re.A使\w不匹配非ASCII字符，等价于re.ASCII
s = "abc中文123"
ret = re.findall(r"\w+", s)
print(ret)
# \w匹配汉字
ret = re.findall(r"\w+", s, re.A)
print(ret)
# \w不匹配汉字

# re.I 使匹配不区分大小写，等价于re.IGNORECASE
s = "Python pYthon python"
print(re.findall(r"python", s))
# 只匹配上了原字符串
print(re.findall(r"python", s, re.I))
# 忽略大小写匹配

# re.S 使 . 匹配包括换行在内的任意字符，等价于re.DOTALL
s = "hello\nworld"
print(re.match(r".+", s).group())
# . 无法匹配\n，只匹配到了 \n 前面的
print(re.match(r".+", s, re.S).group())
# . 可以匹配\n，将输出完整字符串
