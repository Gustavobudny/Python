lista = [
    ("marcelo", 1),
    ("poma", 99),
    ("japa", 22)
]

mais_velho = ("", 0)

for nome, idade in lista:
    if idade > mais_velho[1]:
        mais_velho = (nome, idade)
print(mais_velho)