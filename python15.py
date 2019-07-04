# encoding=UTF-8
str1 = "fewfwegwgwrgwgferhthtrh";
print 'few' in str1, 'few' not in str1  # 有沒有在字串之中
str2 = 'abcde'
str3 = '12345'
print str2 + str3, str2 * 3

print str1[::3]  # 從i到j間隔3取出
print len(str1)
print min(str1)
print max(str1)
print str1.index('gw')
print str1.count('gw')
print str1.count('qq')  # 找到qq的數量為0
