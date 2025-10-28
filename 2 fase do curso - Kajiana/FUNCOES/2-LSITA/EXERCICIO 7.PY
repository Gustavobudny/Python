import math

def hipotenusa():
    a = float(input("Digite o valor do cateto a: "))
    b = float(input("Digite o valor do cateto b: "))
    h = math.sqrt(a**2 + b**2)
    print(f"A hipotenusa é: {h:.2f}")

hipotenusa()