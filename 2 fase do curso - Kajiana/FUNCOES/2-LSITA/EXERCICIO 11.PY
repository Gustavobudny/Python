import random

print("Número aleatório:", random.randint(1, 100))

nomes = ["Ana", "Pedro", "João", "Maria", "Lucas"]
print("Nome escolhido:", random.choice(nomes))

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print("Lista embaralhada:", numeros)
