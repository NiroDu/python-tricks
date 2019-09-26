# part 1
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退

import sys

# iter() 和 next()
list_iter = [1, 2, 3, 4]
it = iter(list_iter)  # 创建迭代器对象
print(next(it))  # 输出 迭代器的下一个元素
print(next(it))
for x in it:
    print(x, end="~ ")


# part 2
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成
# __next__() 方法会返回下一个迭代器对象

# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class MyIterators1:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myIterInstance1 = MyIterators1()
myIterators1 = iter(myIterInstance1)

print(next(myIterators1))
print(next(myIterators1))
print(next(myIterators1))
print(next(myIterators1))
print(next(myIterators1))


# part 3
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyIterators2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myIterInstance2 = MyIterators2()
myIterators2 = iter(myIterInstance2)

for x in myIterators2:
    print(x)
