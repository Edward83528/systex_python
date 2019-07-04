# encoding=UTF-8
class Cour:
    def __init__(self, name, monney):
        self.name = name;
        self.monney = monney;

    def __str__(self):
        return '[%s](%d)' % (self.name, self.monney)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.name == other.name \
               and self.monney == other.monney


c1 = Cour('body', 333);
c2 = c1;

s1 = set();
s1.add(c1)
print s1
s1.add(c2)  # 會認key,所以不會多增加一組
print s1
c3 = Cour('body2', 333);
s1.add(c3)  # 會認不同的key,所以會多增加一組
print s1

print hex(hash(c1)), hex(hash(c2)), hex(hash(c3))

c4 = Cour('body3', 994);
s1.add(c4)

c5 = Cour('body3', 995);
s1.add(c5)
print s1
