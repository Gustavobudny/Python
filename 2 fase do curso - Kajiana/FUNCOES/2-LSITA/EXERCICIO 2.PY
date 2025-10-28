def adicao(numeros):
    return sum(numeros)

def subtracao(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return resultado

def multiplicacao(numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

def divisao(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        resultado /= n
    return resultado

def potenciacao(numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado **= n
    return resultado

def ler_numeros():
    numeros = []
    qtd = int(input("Quantos números deseja inserir? "))
    for i in range(qtd):
        while True:
            try:
                n = float(input(f"Digite o número {i+1}: "))
                numeros.append(n)
                break
            except ValueError:
                print(" Entrada inválida. Digite apenas números.")
    return numeros

def main():
    
    while True:
        print("\n=== Calculadora ===")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potenciação")
        print("0 - Sair")

        escolha = input("Escolha a operação: ")

        if escolha == "0":
            print(" Saindo da calculadora...")
            break

        numeros = ler_numeros()

        if escolha == "1":
            resultado = adicao(numeros)
        elif escolha == "2":
            resultado = subtracao(numeros)
        elif escolha == "3":
            resultado = multiplicacao(numeros)
        elif escolha == "4":
            resultado = divisao(numeros)
        elif escolha == "5":
            resultado = potenciacao(numeros)
        else:
            print(" Opção inválida!")
            continue

        if resultado is not None:
            print(f" Resultado: {resultado}")

        continuar = input("\nDeseja realizar outro cálculo? (s/n): ").lower()
        if continuar != "s":
            print("👋 Até logo!")
            break

# Executar o programa
main()
