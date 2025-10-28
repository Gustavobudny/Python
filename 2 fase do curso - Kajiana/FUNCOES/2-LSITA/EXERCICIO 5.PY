reservas = []

def adicionar_reserva():
    destino = input("Digite o destino: ")
    data = input("Digite a data da viagem: ")
    passageiros = int(input("Digite o número de passageiros: "))
    reservas.append({"destino": destino, "data": data, "passageiros": passageiros})
    print("Reserva adicionada!")

def visualizar_reservas():
    if not reservas:
        print("Nenhuma reserva feita.")
    else:
        for r in reservas:
            print(f"Destino: {r['destino']} - Data: {r['data']} - Passageiros: {r['passageiros']}")

def menu_reservas():
    while True:
        print("\n===== SISTEMA DE RESERVAS =====")
        print("1 - Adicionar reserva")
        print("2 - Visualizar reservas")
        print("3 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_reserva()
        elif opcao == "2":
            visualizar_reservas()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")
            
menu_reservas()