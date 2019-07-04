# encoding=UTF-8
a = 5
b = 7
print "a=%d b=%d" % (a, b)
temp = a
a = b
b = temp
print "a=%d b=%d" % (a, b)
c = 6
d = 8
print "c=%d b=%d" % (c, d)
c, d = b, c
print "c=%d b=%d" % (c, d)
e = "hello word"
f = 3.14
print "e=%s ,f=%.3f" % (e, f)
print "e={},f={}".format(e, f)
l1 = 'A'
l2 = 'B'
l3 = 'C'
l4 = 'D'
print l1, l2, l3, l4
