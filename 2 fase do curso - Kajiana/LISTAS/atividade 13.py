lista_tarefa = []

while True:
    print('escolha uma das opções de sua lista de tarefas: \n' 
    'a) adicione um item a lista\n' 
    'b) remove um item na lista\n' 
    'c) mostrar todos os itens de uma lista \n' 
    'd) mostrar um item especifico da lista \n' 
    'e) sair das opcoes')

    op = input('digite sua opcao: ')

    if op == 'a':
        item = input('digite seu item a lista: ')
        lista_tarefa.append(item)
    elif op == 'b':
        remove = input('digite o item que voce deseja excluir: ')
        lista_tarefa.remove(remove)
    elif op == 'c':
        print(lista_tarefa)
    elif op == 'd':
        n = int(input('em ordem numerica, fale o item que deseja mostrar: '))
        print(lista_tarefa[n])
    elif op == 'e':
        print('acabou')
        break
    else:
        print('erro, tente novamente1!!')