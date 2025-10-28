
def adicionar_tarefa(tarefas):
    """
    Função para adicionar uma nova tarefa à lista.
    """
    tarefa = input("Digite a descrição da tarefa: ")
    id_tarefa = len(tarefas) + 1
    tarefas.append({'id': id_tarefa, 'tarefa': tarefa, 'status': 'pendente'})
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas(tarefas):
    """
    Função para visualizar todas as tarefas da lista.
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nLista de Tarefas:")
    for t in tarefas:
        print(f"ID: {t['id']}, Tarefa: {t['tarefa']}, Status: {t['status']}")

def atualizar_tarefa(tarefas):
    """
    Função para atualizar uma tarefa existente.
    """
    if not tarefas:
        print("Nenhuma tarefa para atualizar.")
        return
    try:
        id_tarefa = int(input("Digite o ID da tarefa a atualizar: "))
        for t in tarefas:
            if t['id'] == id_tarefa:
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                t['tarefa'] = nova_tarefa
                print("Tarefa atualizada com sucesso!")
                return
        print("ID da tarefa não encontrado.")
    except ValueError:
        print("ID inválido. Digite um número.")

def excluir_tarefa(tarefas):
    """
    Função para excluir uma tarefa da lista.
    """
    if not tarefas:
        print("Nenhuma tarefa para excluir.")
        return
    try:
        id_tarefa = int(input("Digite o ID da tarefa a excluir: "))
        for i, t in enumerate(tarefas):
            if t['id'] == id_tarefa:
                tarefas.pop(i)
                print("Tarefa excluída com sucesso!")
                return
        print("ID da tarefa não encontrado.")
    except ValueError:
        print("ID inválido. Digite um número.")

def main():
    """
    Função principal que executa o menu do sistema.
    """
    tarefas = []
    while True:
        print("\n--- Sistema de Gerenciamento de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Atualizar tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        opcao = input("Escolha uma opção (1-5): ")
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            atualizar_tarefa(tarefas)
        elif opcao == '4':
            excluir_tarefa(tarefas)
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()