lista_num = []
lista_par = []
lista_impar = []
lista_primo = []


while True:

    print('selecione uma das opções para sua lista: ')

    print('a. Adicionar um número: Permita ao usuário adicionar um número à lista\nb. Remover um número: Permita ao usuário remover um número específico da lista\nc. Exibir todos os números: Liste todos os números atualmente na lista.\nd. Exibir somente números pares: Liste apenas os números pares presentes na lista, um embaixo do outro.\ne. Exibir somente números ímpares: Liste apenas os números ímpares presentes na lista, um embaixo do outro\nf. Exibir somente números primos: Liste apenas os números primos presentes na lista, um embaixo do outro.\ng. sair do menu de opcoes\n')

    op = input('digite sua opcao de escolha: ')

    if op == 'a':
        num = int(input('digite um numero que voce deseja adicionar a lista: '))
        lista_num.append(num)
    elif op == 'b':
        esc = input('escolha o numero que voce deseja excluir da sua lista: ')
        lista_num.remove(esc)
    elif op == 'c':
        print(lista_num)
    elif op == 'd':
        for i in lista_num:
            if i %2 == 0:
                lista_par.append(i)
                print(f'os seus numero pares sao: {lista_par}')
    elif op == 'e':
        for i in lista_num:
            if i %2 != 0:
                lista_impar.append(i)
                print(f'seus numero impares sao: {lista_impar}')
    elif op == 'f':

        divisor = 0

        for i in range(1,(len(lista_num))):
            if len(lista_num) % i == 0:
                divisor += 1
            elif divisor == 2:
                lista_primo.append(i)
                print(lista_primo)
    elif op == 'g':
        break

    else:
        print('ocorreu algum erro tente novamente')
        
            
