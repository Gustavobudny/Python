def numero_na_lista(lista, numero):
    return numero in lista

lista = [1, 3, 5, 7, 9]
num = int(input("Digite um número para verificar se está na lista [1, 3, 5, 7, 9]: "))

print("Resultado:", numero_na_lista(lista, num))
