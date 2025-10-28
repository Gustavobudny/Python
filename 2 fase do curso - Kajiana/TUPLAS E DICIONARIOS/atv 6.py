mercado = {"caneta": (2.50, 10), "caderno": (15.00, 5), "borracha": (1.00, 20) }

op = input('digite o item que voce deseja buscar: ')

for i in mercado.keys():
    if i == op:
        v,f = mercado[i]
        vf = v * f
        print(vf)
