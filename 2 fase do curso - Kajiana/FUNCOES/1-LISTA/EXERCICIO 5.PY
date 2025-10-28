def soma_maior_que_limite(a, b, limite):
    return (a + b) > limite

x = float(input("Digite o primeiro número (a): "))
y = float(input("Digite o segundo número (b): "))
limite = float(input("Digite o valor do limite: "))

print("Resultado:", soma_maior_que_limite(x, y, limite))

