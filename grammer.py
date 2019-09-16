# 单行注释

"""
多行注释
"""

if True:
    print("True")
elif False:
    print("elif")
else:
    print("False")

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
string = 'Runoob'
print(string)  # 输出字符串
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符
print(string[0])  # 输出字符串第一个字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string[2:])  # 输出从第三个开始的后的所有字符
print(string * 2)  # 输出字符串两次
print(string + '你好')  # 连接字符串

# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
print(r"this is a line with \n")

# 内置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a1 = set('abracadabra')
print(a1)

dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
dict2 = {x: x**2 for x in (2, 4, 6)}
dict3 = dict(Runoob=1, Google=2, Taobao=3)

print(dict1)
print(dict2)
print(dict3)

if __name__ == '__main__':
    input("\n\n按下 enter 键后退出。")
