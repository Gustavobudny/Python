#4. Ordene uma lista de tuplas com nome e idade usando
#lambda.

pessoas = [("Gustavo", 16), ("Poma", 15), ("Davi", 4)]

idade = sorted(pessoas, key=lambda x: x[1])

print(idade)

nome = sorted(pessoas, key=lambda x: x[0])

print(nome)