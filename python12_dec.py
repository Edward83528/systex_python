# encoding=UTF-8
from decimal import Decimal

print Decimal(2.968)
print Decimal('2.968')
print Decimal(2.968) - Decimal(2968) * Decimal(0.001)#有誤差
print Decimal('2.968') - Decimal(2968) * Decimal('0.001')#無誤差
