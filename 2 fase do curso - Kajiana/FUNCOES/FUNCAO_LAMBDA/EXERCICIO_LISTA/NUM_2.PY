from functools import reduce

operacoes = {
    "1": lambda nums: reduce(lambda x, y: x + y, nums),
    "2": lambda nums: reduce(lambda x, y: x - y, nums),
    "3": lambda nums: reduce(lambda x, y: x * y, nums),
    "4": lambda nums: reduce(lambda x, y: x / y if y != 0 else float('inf'), nums),
    "5": lambda nums: reduce(lambda x, y: x ** y, nums)
}

ler_numeros = lambda: [float(input(f"Digite o número {i+1}: ")) for i in range(int(input("Quantos números deseja inserir? ")))]

def main():
    while True:
        print("\n=== Calculadora ===")
        print("1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | 5 - Potenciação | 0 - Sair")

        escolha = input("Escolha: ")
        if escolha == "0":
            print("BYEE BYEE")
            break

        if escolha in operacoes:
            nums = ler_numeros()
            resultado = operacoes[escolha](nums)
            print("Resultado:", resultado)
        else:
            print("Opção inválida!")

main()
