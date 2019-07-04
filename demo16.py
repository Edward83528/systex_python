# encoding=UTF-8
x1 = 'abcde'
x2 = ['a', 'b', 'c', 'd', 'e']
print type(x1), len(x1)
print type(x2), len(x2)
print x1[0], x2[0]

x2[0] = 'm'  # 可變的
print x1[0], x2[0]

# x1[0] = 'm'  # 不可變的
# print x1[0], x2[0]
