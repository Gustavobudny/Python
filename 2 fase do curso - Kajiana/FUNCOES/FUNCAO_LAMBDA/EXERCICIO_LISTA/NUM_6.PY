import math

hipotenusa = lambda a, b: math.sqrt(a ** 2 + b ** 2)

cateto_1 = float(input("digite seu cateto 1: "))
cateto_2 = float(input("digite seu cateto 2: "))


c = hipotenusa(cateto_1, cateto_2)

print(c)