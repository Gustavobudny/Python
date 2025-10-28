import math

num = float(input("Digite um número positivo: "))
print("Raiz quadrada:", math.sqrt(num))

angulo = float(input("Digite um ângulo em graus: "))
rad = math.radians(angulo)
print("Seno do ângulo:", math.sin(rad))

decimal = float(input("Digite um número decimal: "))
print("Arredondado para cima:", math.ceil(decimal))
print("Arredondado para baixo:", math.floor(decimal))
