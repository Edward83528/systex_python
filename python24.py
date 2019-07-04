left = ['A', 'B']
right = ['C', 'D']
p1 = [left, right]
p2 = p1;

import copy

p3 = copy.copy(p1)
p4 = copy.deepcopy(p2)
p1.append('7')
p1[0][0] = 'Joker'
print p1, p2, p3, p4
