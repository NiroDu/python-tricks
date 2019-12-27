# 继承
# 类定义


# BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
# class DerivedClassName(otherModname.BaseClassName):

class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        # 调用父类的构函
        People.__init__(self, name, age, weight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


student_instance = Student('student_instance', 18, 120, 3)
student_instance.speak()


# 另一个类，多重继承之前的准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, name, age, weight, grade, topic):
        Student.__init__(self, name, age, weight, grade)
        Speaker.__init__(self, name, topic)


test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前的父类的方法，排前的！
