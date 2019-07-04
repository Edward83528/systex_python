# encoding=UTF-8
class Cours:
    def __init__(self, name, time):
        self.name = name;
        self.time = time;

    def __str__(self):
        return '[Cours](name=%s)(time=%d)' % (self.name, self.time)

    def __repr__(self):
        return '[Cours](name=%s\n)(time=%s\n)' % (self.name, self.time)


c1 = Cours('chinese', 4);
c2 = Cours('english', 7);
print 'c1=%s,c2=%s' % (c1, c2)  # __str__的用法
print c1  # __str__的用法
print [c1]  # __repr__的用法
print '分別%s,%r' % (c1, c2)  # 印出r和s
print '同時{0!s},{0!r}'.format(c1)  # 同時印出r和s
