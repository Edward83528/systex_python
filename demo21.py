# encoding=UTF-8
print '%-10s===' % '0123456789'
print '%-10s===' % '0123456789'[:5]
print '%-10s===' % ('0123456789' * 2)
for i in range(0, 5):
    print '%*s===' % (((-10 - 5 * i), 'ok!'));
# print '{:<10s}==='.format('0123456789')
for i in range(0, 5):
    print '{:<{}s}==='.format('012',10+5*i)
