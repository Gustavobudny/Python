estoque = {}

while True:
    print("\n=== Sistema de Estoque ===")
    print("a) Adicionar produto")
    print("b) Atualizar quantidade")
    print("c) Calcular valor total do estoque")
    print("d) Listar todos os produtos")
    print("e) Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "a":
        nome = input("Nome do produto: ")
        if nome in estoque:
            print("Produto já existe.")
        else:
            preco_input = input("Preço do produto: R$")
            quantidade_input = input("Quantidade: ")

            if preco_input.replace('.', '', 1).isdigit() and quantidade_input.isdigit():
                preco = float(preco_input)
                quantidade = int(quantidade_input)
                estoque[nome] = {"preço": preco, "quantidade": quantidade}
                print(f"Produto '{nome}' adicionado com sucesso!")
            else:
                print("Erro: preço e quantidade devem ser números válidos.")

    elif opcao == "b":
        nome = input("Nome do produto: ")
        if nome in estoque:
            nova_qtd_input = input("Nova quantidade: ")
            if nova_qtd_input.isdigit():
                nova_qtd = int(nova_qtd_input)
                estoque[nome]["quantidade"] = nova_qtd
                print(f"Quantidade de '{nome}' atualizada para {nova_qtd}.")
            else:
                print("Erro: quantidade inválida.")
        else:
            print("Produto não encontrado.")

    elif opcao == "c":
        total = 0
        for item in estoque.values():
            total += item["preço"] * item["quantidade"]
        print(f"Valor total do estoque: R${total:.2f}")

    elif opcao == "d":
        if not estoque:
            print("Estoque vazio.")
        else:
            print("Produtos no estoque:")
            for nome, dados in estoque.items():
                print(f"- {nome}: Preço R${dados['preço']:.2f}, Quantidade {dados['quantidade']}")

    elif opcao == "e":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
        