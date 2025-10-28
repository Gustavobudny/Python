#3. Ordene lista de dicionários por idade

pessoas = [("Gustavo", 16), ("Poma", 15), ("Davi", 4)]

idade = sorted(pessoas, key=lambda x: x[1])

print(idade)