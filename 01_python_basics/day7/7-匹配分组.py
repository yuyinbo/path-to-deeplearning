# 作者: 余殷博
# cangj87@gmail.com
import re

# |表示匹配左右任意一个
# 匹配0到100
ret = re.match(r"[1-9]\d$|100", "100")
print(ret.group())

email_list = ['example@163.com', 'example@qq.com', 'example@gmail.com']
for email in email_list:
    ret = re.match(r'\w{5,20}@(163|gmail|hotmail)\.com$', email)
    # 小括号()用于分组，也可以和 | 配合表示“或”
    # 这里表示匹配163或gmail或hotmail
    # 如果不加小括号，则表示匹配'\w{5,20}@163'或"gmail"或"hotmail\.com$"
    if ret:
        print(f'{email}是合法的邮箱')
    else:
        print(f'{email}不是合法的邮箱')

# 匹配电话号码
ret = re.match(r"([^-]+)-(\d+)", "03-12345678")
"[]表示字符集合，^表示取反，[^-]+表示匹配一个到多个非-字符"
print(ret.group())
print(ret.group(1))
print(ret.group(2))
# group(n)返回第n个分组


# 引用分组
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
# ()表示将其中内容捕获为分组，\1表示引用第一个分组
if ret:
    print(ret.group())
else:
    print("标签对匹配失败")
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html1>")
if ret:
    print(ret.group())
else:
    print("标签对匹配失败")
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",
               '<html><h1>www.google.com</h1></html>')
if ret:
    print(ret.group())
else:
    print("标签对匹配失败")

# 给分组起别名
ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>",
               '<html><h2>www.baidu.com</h2></html>')
# 语法(?P<name>.*)表示命名此分组为name
# ?表示这个分组有特殊功能，P表示它是一个命名分组，name表示命名分组的名称
# (?P=name)表示引用name分组
if ret:
    print(ret.group())
    print(ret.group("name1"))
    print(ret.group("name2"))
else:
    print("标签对匹配失败")