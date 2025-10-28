import math

# Funções para calcular áreas
def area_circulo(raio):
    return math.pi * (raio ** 2)

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

# Programa principal
def menu():
    while True:
        print("\n===== CALCULADORA DE ÁREAS =====")
        print("1 - Área do Círculo")
        print("2 - Área do Retângulo")
        print("3 - Área do Triângulo")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            raio = float(input("Digite o raio do círculo: "))
            print(f"A área do círculo é: {area_circulo(raio):.2f}")

        elif opcao == "2":
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            print(f"A área do retângulo é: {area_retangulo(base, altura):.2f}")

        elif opcao == "3":
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            print(f"A área do triângulo é: {area_triangulo(base, altura):.2f}")

        elif opcao == "4":
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente!")

# Executar programa
menu()
