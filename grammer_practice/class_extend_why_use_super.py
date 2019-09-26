# 经典的菱形继承案例，BC 继承 A，然后 D 继承 BC，创造一个 D 的对象
#      ---> B ---
# A --|          |--> D
#      ---> C ---

# 使用 super() 可以很好地避免构造函数被调用两次。

# 先是不使用super()看看效果：
class A:
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        A.__init__(self)
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        A.__init__(self)
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        B.__init__(self)
        C.__init__(self)
        print('leave D')


d = D()

# enter D
# enter B
# enter A
# leave A
# leave B
# enter C
# enter A
# leave A
# leave C
# leave D

# 再使用super()看看输出
# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')
#
#
# class B(A):
#     def __init__(self):
#         print('enter B')
#         super().__init__()
#         print('leave B')
#
#
# class C(A):
#     def __init__(self):
#         print('enter C')
#         super().__init__()
#         print('leave C')
#
#
# class D(B, C):
#     def __init__(self):
#         print('enter D')
#         super().__init__()
#         print('leave D')
#
#
# d = D()
# enter D
# enter B
# enter C
# enter A
# leave A
# leave C
# leave B
# leave D
