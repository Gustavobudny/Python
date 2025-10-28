#5. Use lambda com sorted() para ordenar strings
#ignorando maiúsculas.

palavras = ["pao", "arroz", "davi", "japa"]

ordem = sorted(palavras, key=lambda x: x.lower())

print("Ordenado ignorando maiúsculas:", ordem)