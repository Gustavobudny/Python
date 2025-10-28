frase = input('digite uma frase: ').lower()

palavras = frase.split()

dicionario = { }

for p in palavras:
    if p in dicionario:
        dicionario[p] += 1
    else:
        dicionario[p] = 1

print(dicionario)



