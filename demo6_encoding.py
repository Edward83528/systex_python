# encoding=UTF-8
x1 = "hello word"
print(type(x1), x1)
x2 = u"hello word"
print(type(x2), x2)
x3 = b"hello word"
print(type(x3), x3)
x4 = "加個中文"#沒加encoding=UTF-8 時Non-ASCII character '\xe5'
print len(x4),type(x4), x4
x5 = u"加個中文"
print len(x5),type(x5), x5