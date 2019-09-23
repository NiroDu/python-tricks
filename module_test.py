import sys


def go():
    print('命令行参数如下:')
    # sys.argv 是一个包含命令行参数的列表。（命令行里输入的参数）
    for i in sys.argv:
        print(i)
    # sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
    print('\n\nPython 路径为：', sys.path, '\n')


def create_file():
    # 打开一个文件
    f = open("/Users/xmly/github/python-tricks/foo.txt", "r")
    file_content = f.read()
    # file_lines_content = f.readlines()
    print(file_content)
    # print(file_lines_content)
    # f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

    # 关闭打开的文件
    f.close()


if __name__ == '__main__':
    # go()
    create_file()
