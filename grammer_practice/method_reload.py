# 如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
# super() 函数是用于调用父类(超类)的一个方法。
class Parent:  # 定义父类
    def my_method(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def my_method(self):
        print('调用子类方法')


child_instance = Child()  # 子类实例
child_instance.my_method()  # 子类调用重写方法
super(Child, child_instance).my_method()  # 用子类对象调用父类已被覆盖的方法
