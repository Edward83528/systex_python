# encoding=UTF-8
sale = {'s1': 300, 's2': 9, 's3': 8}
print type(sale), sale  # <type 'dict'> {'s3': 8, 's2': 9, 's1': 300}
print sale['s1'], sale['s2'], sale['s3']
# print sale['s4']#KeyError 不能印出不存在的值
sale['s5'] = 863  # 但能加新的值
print sale  # {'s3': 8, 's2': 9, 's1': 300, 's5': 863}
print sale.get('s2'), sale.get('s6'), sale.get('s6', '不存在')  # 有值傳回vale沒值傳回None,可取代預設值
print 's2' in sale, 'xxx' in sale  # True False用in決定存不存在
print [e for e in sale]  # ['s3', 's2', 's1', 's5']
print [e for e in sale.keys()]  # ['s3', 's2', 's1', 's5']
print [e for e in sale.values()]  # [8, 9, 300, 863]
for t in sale.items():
    print type(t), t  # <type 'tuple'> ('s3', 8)
updatestr = {'s2': 999999}
sale.update(updatestr)  # 更新字典
print sale

for i in sale.items():
    print i[0], i[1]  # 印出key value
for i1, i2 in sale.items():  # 第二種寫法印出key value
    print "i1=%s,i2=%s" % (i1, i2)
