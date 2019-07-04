# encoding=UTF-8
"""
round python3解法

"""
from decimal import Decimal,ROUND_HALF_UP,ROUND_HALF_EVEN

value=Decimal(2.5)

result=Decimal(value.quantize(Decimal(1),rounding=ROUND_HALF_UP))
print(result)

result2=Decimal(value.quantize(Decimal(1),rounding=ROUND_HALF_EVEN))
print(result2)
