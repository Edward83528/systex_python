# encoding=UTF-8
l1 = list('appale')
t1 = tuple('appale')
s1 = set(list('appale'))
s2 = {'a', 'p', 'p', 'a', 'l', 'e'}
s3 = {'b', 'a', 'n', 'n', 'a', 'e'}
print l1, type(l1)
print t1, type(t1)
print s1, type(s1)  # set會自動過濾掉相同元素

print s2 | s3, len((s2 | s3))
print s2 & s3, len((s2 & s3))
print s2 ^ s3, len((s2 ^ s3))

# s2.add(s3)#TypeError: unhashable type: 'set' 要設不可變的集合,是可變的
for e in s3:
    s2.add(e)  # set加到另一個set
print s2
