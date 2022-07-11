import math
print(format(math.pi, '.12g'))  # give 12 significant digits
print(format(math.pi, '.2f'))   # give 2 digits after the point
print(repr(math.pi))
print(.1 + .1 + .1 == .3)
print(round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1))
print(round(.1 + .1 + .1, 10) == round(.3, 10))
x = 3.14159
print(x.as_integer_ratio())
print(x == 3537115888337719 / 1125899906842624)
print(x.hex())
print(x == float.fromhex('0x1.921f9f01b866ep+1'))
print(sum([0.1] * 10) == 1.0)
print(math.fsum([0.1] * 10) == 1.0)
print("hola")