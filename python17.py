# encoding=UTF-8
x1 = list('abcdef')  # 字串不能被更改所以把她轉型
x1[::2] = '*' * len(x1[::2])  # *會有長度/2個

x3 = ['A', 'B', 'C', 'D', 'E']
x4 = ['a', 'b', 'c', 'd', 'e']
x3.append(x4)  # 不管是什麼東西就放最後面
print(x3)

x5 = ['A', 'B', 'C', 'D', 'E']
x6 = ['a', 'b', 'c', 'd', 'e']
x5.extend(x6);  # 跟+=有點像
print(x5)

x7 = ['A', 'B', 'C', 'D', 'E']
x8 = ['a', 'b', 'c', 'd', 'e']
x7 += x8
print(x7)

x8 = list('jffoeuenclf')
x8.sort()
print x8

x9 = list('jffAoeuGencJlf')
x9.sort()
print x9

