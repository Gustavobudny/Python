#2. Use lambda com map() para dobrar os números
#de uma lista.

nuns = [1, 2, 3, 5 ,6, 7]

dobrado = list(map (lambda x: x * 2, nuns))

print(dobrado)