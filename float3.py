print(2**52 <=  2**56 // 10  < 2**53)
q, r = divmod(2**56, 10)
print('q= ',q,'\nr= ',r)
print(q+1)
c, r2 = divmod(2**55, 5)
print('cociente: ',c,'\nresto: ',r2)
print(7205759403792794 / 2 ** 56)
print(3602879701896397 / 2 ** 55)
print(0.1 * 2 ** 55)
print(3602879701896397 * 10 ** 55 // 2 ** 55)
print(format(0.1, '.17f'))
from decimal import Decimal
from fractions import Fraction
print(Fraction.from_float(0.1))
print((0.1).as_integer_ratio())
print(Decimal.from_float(0.1))
print(format(Decimal.from_float(0.1), '.17'))