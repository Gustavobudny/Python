def soma_ate_n(n):
    if n <= 0:
        return "O número deve ser inteiro positivo."
    
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

numero = int(input("Digite um número inteiro positivo: "))
print(f"A soma de todos os inteiros positivos até {numero} é {soma_ate_n(numero)}")