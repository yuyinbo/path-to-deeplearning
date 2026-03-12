# 作者: 余殷博
# cangj87@gmail.com


def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


def sum_2_num(num1, num2):
    result = num1 + num2
    print(f'{num1}+{num2}={result}')


print('调用前')  # 此时用步入而不是步过才能逐句输出
say_hello()  # 运行时是逐行解释，所以函数调用必须在定义后面
print('调用后0')
print('调用后1')
print('调用后2')

sum_2_num(1, 2)
