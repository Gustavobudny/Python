agenda = {}

while True:
    print("\n=== Agenda de Contatos ===")
    print("a) Adicionar contato")
    print("b) Buscar contato por nome")
    print("c) Remover contato")
    print("d) Exibir todos os contatos em ordem alfabética")
    print("e) Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "a":
        nome = input("Nome do contato: ")
        if nome in agenda:
            print("Contato já existe.")
        else:
            telefone = input("Telefone: ")
            email = input("Email: ")
            if telefone.strip() != "" and email.strip() != "":
                agenda[nome] = {"telefone": telefone, "email": email}
                print(f"Contato '{nome}' adicionado com sucesso!")
            else:
                print("Telefone e email não podem estar vazios.")

    elif opcao == "b":
        nome = input("Digite o nome do contato que deseja buscar: ")
        if nome in agenda:
            print(f"Nome: {nome}")
            print(f"Telefone: {agenda[nome]['telefone']}")
            print(f"Email: {agenda[nome]['email']}")
        else:
            print("Contato não encontrado.")

    elif opcao == "c":
        nome = input("Digite o nome do contato que deseja remover: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "d":
        if not agenda:
            print("Agenda vazia.")
        else:
            print("Contatos em ordem alfabética:")
            for nome in sorted(agenda.keys()):
                print(f"- {nome}: Telefone: {agenda[nome]['telefone']}, Email: {agenda[nome]['email']}")

    elif opcao == "e":
        print("Encerrando a agenda...")
        break

    else:
        print("Opção inválida. Tente novamente.")


