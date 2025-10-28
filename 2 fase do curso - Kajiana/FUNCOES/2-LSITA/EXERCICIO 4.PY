agenda = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone: ")
    agenda.append({"nome": nome, "telefone": telefone})
    print("Contato adicionado com sucesso!")

def visualizar_contatos():
    if not agenda:
        print("Nenhum contato na agenda.")
    else:
        for c in agenda:
            print(f"Nome: {c['nome']} - Telefone: {c['telefone']}")

def editar_contato():
    nome = input("Digite o nome do contato a editar: ")
    for c in agenda:
        if c["nome"] == nome:
            novo_tel = input("Digite o novo telefone: ")
            c["telefone"] = novo_tel
            print("Contato atualizado!")
            return
    print("Contato não encontrado.")

def excluir_contato():
    nome = input("Digite o nome do contato a excluir: ")
    for c in agenda:
        if c["nome"] == nome:
            agenda.remove(c)
            print("Contato excluído!")
            return
    print("Contato não encontrado.")

def menu_agenda():
    while True:
        print("\n===== AGENDA DE CONTATOS =====")
        print("1 - Adicionar contato")
        print("2 - Visualizar contatos")
        print("3 - Editar contato")
        print("4 - Excluir contato")
        print("5 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            visualizar_contatos()
        elif opcao == "3":
            editar_contato()
        elif opcao == "4":
            excluir_contato()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

