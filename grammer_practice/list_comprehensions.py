# 列表推导式
# 把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列。

vec = [2, 4, 6]
# 我们将列表中每个数值乘三，获得一个新的列表：
print([3*x for x in vec])
# 输出：[6, 12, 18]

print([[x, x**2] for x in vec])
# 输出：[[2, 4], [4, 16], [6, 36]]

# 我们可以用 if 子句作为过滤器：
print([3*x for x in vec if x > 3])
# 输出：[12, 18]

print([3*x for x in vec if x < 2])
# 输出：[]

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print([x * y for x in vec1 for y in vec2])
# 输出：[8, 6, -18, 16, 12, -36, 24, 18, -54]

print([x + y for x in vec1 for y in vec2])
# 输出：[6, 5, -7, 8, 7, -5, 10, 9, -3]

print([vec1[i] * vec2[i] for i in range(len(vec1))])
# 输出：[8, 12, -54]

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# 等价于
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
# combs

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
# 输出：[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

