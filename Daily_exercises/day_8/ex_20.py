# calculates how much paint is needed

import math
a = int(input("a: "))
b = int(input("b: "))
coverage = 5

def paint_cal(a, b, cover):
    return math.ceil(a*b/cover)

print(paint_cal(a, b, coverage))


