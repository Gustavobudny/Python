import math

area_circulo = lambda r: math.pi * (r ** 2)
area_retangulo = lambda b, h: b * h
area_triangulo = lambda b, h: (b * h) / 2

def menu():
    opcoes = {
        "1": lambda: print(f"A área do círculo é: {area_circulo(float(input('Raio: '))):.2f}"),
        "2": lambda: print(f"A área do retângulo é: {area_retangulo(float(input('Base: ')), float(input('Altura: '))):.2f}"),
        "3": lambda: print(f"A área do triângulo é: {area_triangulo(float(input('Base: ')), float(input('Altura: '))):.2f}"),
        "4": lambda: exit("tchauuuuuuu")
    }

    while True:
        print("\n CALCULADORA DE ÁREAS ")
        print("1 - Círculo\n2 - Retângulo\n3 - Triângulo\n4 - Sair")
        escolha = input("Escolha: ")
        opcoes.get(escolha, lambda: print("Opção inválida!"))()

menu()