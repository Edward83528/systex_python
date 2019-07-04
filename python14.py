# encoding=UTF-8
str1 = "fewfwegwgwrgwgferhthtrh";
print str1[0], str1[len(str1) - 1]
print str1[-1], str1[-len(str1)]
print str1[0:5], str1[:5]
print str1[-5:-1], str1[-5:]

str2 = "www.com.tw"
str3 = str2.split('.')
print str3  # ['www', 'com', 'tw']
print '!'.join(str3)  # www!com!tw
