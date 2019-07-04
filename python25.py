day = {'sun', 'mons'}
length = []
for i in day:
    length.append(len(i))
    pass
print length

print [len(da) for da in day]
print [da for da in day if len(da) > 3]

number_list = [1, 3, 2, 6, 1]
s1 = sorted(e for e in number_list if e > 2)
print s1
s2 = sorted((e for e in number_list if e > 2), reverse=True)
print s2
