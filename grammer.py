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
dict2 = {x: x ** 2 for x in (2, 4, 6)}
dict3 = dict(Runoob=1, Google=2, Taobao=3)

print(dict1)
print(dict2)
print(dict3)

a_string = 'Hello'

print('截取后的string:', a_string[1:4])
print("我叫%s，今年%d岁!" % ('小明', 10))

for i in range(5, 9):
    print(i)

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, value)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#  元组 不需要括号也可以
tup3 = "a", "b", "c", "d"
tup4 = tup3, (1, 2, 3, 4, 5)
print(tup3)
print('{0}'.format(tup4))

# 迭代器
list_iter = [1, 2, 3, 4]
it = iter(list_iter)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))
for x in it:
    print(x, end=" ")

print('\n分隔符')


# __iter__() 方法返回一个特殊的迭代器对象
# __next__() 方法会返回下一个迭代器对象

class MyNumbers:
    def __iter__(self):
        self.a = 6
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


instanceClass = MyNumbers()
instanceIter = iter(instanceClass)

# print(next(instanceIter))
for x in instanceIter:
    print(x)

if __name__ == '__main__':
    input("\n\n按下 enter 键后退出。")
