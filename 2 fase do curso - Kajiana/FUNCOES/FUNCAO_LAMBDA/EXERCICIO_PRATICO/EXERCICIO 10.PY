#5. Crie função operador que retorna soma,
#subtração, etc.

def operador(a, b, op):
    operacoes = {
        "soma": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mult": lambda x, y: x * y,
        "div": lambda x, y: x / y if y != 0 else "Erro: divisão por zero"
    }
    return operacoes.get(op, lambda x, y: "Operação inválida")(a, b)

print(operador(10, 5, "soma"))
print(operador(10, 5, "sub"))
print(operador(10, 5, "mult"))
print(operador(10, 5, "div"))
print(operador(10, 0, "div"))
print(operador(10, 5, "pot"))

