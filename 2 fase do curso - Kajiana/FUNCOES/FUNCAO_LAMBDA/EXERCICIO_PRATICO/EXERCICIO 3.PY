#3. Use lambda com filter() para obter os
#números maiores que 5.

numeros = [1, 2, 3, 6, 8, 10]

maiores_que_5 = list(filter(lambda x: x > 5, numeros))

print(maiores_que_5)
