# encoding=UTF-8
l1 = ['sunday', 'monday']  # list
t1 = ('sunday', 'monday')  # tuple
print type(l1), type(t1), len(l1), len(t1)
print [len(e) for e in l1]
print [len(e) for e in t1]
print "list前", (hex(id(l1)))
l1.append('ggggggg')  # list不可變要用append的方式
print "list後", (hex(id(l1)))  # list前後指向相同記憶體
print "tuple前", (hex(id(t1)))
t1 += ('eeeeeeeee',)  # tuple只能跟tuple相加
print "tuple後", (hex(id(t1)))  # tuple前後指向不同記憶體
print l1
print t1

s2 = ('king')  # <type 'str'>
t2 = ('king',)  # <type 'tuple'>
print type(s2), type(t2)
print s2 * 5  # str會串接
print t2 * 5  # tuple元素會變多

print len(l1), t1[0]
print 'ki' in s2
print 'ki' in t2, 'king' in t2  # tuple元素是獨立個體要整個比對才會為true


def split_head(x):
    return x[0], x[1:]


head, rema = split_head(l1)
print type(rema), len(rema), rema
print type(head), len(head), head
