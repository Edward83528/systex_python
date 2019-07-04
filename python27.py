# encoding=UTF-8
r1 = range(0, 10)  # 0~9
print type(r1), r1, len(r1)

r2 = range(0, 10, 2)  # 0~9 step為2兩個跳一次
print type(r2), r2, len(r2)

import math

r4 = range(0, int(5 * math.pi))
print r4

import numpy as np

r5 = np.arange(0, 10)
print type(r5), r5, len(r5)  # <type 'numpy.ndarray'>用numpy來range浮點數

print r1 + r5
r6 = np.arange(0, math.pi, 0.05)
print r6

r7 = np.linspace(0, 10)  # 包頭也包尾,預設切50刀
print type(r7), r7, len(r7)

r8 = np.linspace(0, 10, 51)  # 包頭也包尾,要精準一點就多切一刀
print type(r8), r8, len(r8)

r9 = np.linspace(0, np.pi)  # 包頭也包尾,要精準一點
print type(r9), r9, len(r9)
