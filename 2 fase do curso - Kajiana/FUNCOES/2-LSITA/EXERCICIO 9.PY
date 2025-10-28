def cadastrar_nota(alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota
    print(f"Nota cadastrada para {nome}!")

def alterar_nota(alunos):
    nome = input("Digite o nome do aluno que deseja alterar a nota: ")
    if nome in alunos:
        nova_nota = float(input(f"Digite a nova nota de {nome}: "))
        alunos[nome] = nova_nota
        print("Nota alterada com sucesso!")
    else:
        print("Aluno não encontrado!")

def excluir_nota(alunos):
    nome = input("Digite o nome do aluno que deseja excluir: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido com sucesso!")
    else:
        print("Aluno não encontrado!")

def exibir_notas(alunos):
    if alunos:
        print("\n--- Notas dos alunos ---")
        for nome, nota in alunos.items():
            print(f"{nome}: {nota}")
    else:
        print("Nenhum aluno cadastrado!")

def calcular_media(alunos):
    if alunos:
        media = sum(alunos.values()) / len(alunos)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhum aluno cadastrado!")

def main():
    alunos = {}
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar Nota")
        print("2 - Alterar Nota")
        print("3 - Excluir Nota")
        print("4 - Exibir Notas")
        print("5 - Calcular Média da Turma")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_nota(alunos)
        elif opcao == "2":
            alterar_nota(alunos)
        elif opcao == "3":
            excluir_nota(alunos)
        elif opcao == "4":
            exibir_notas(alunos)
        elif opcao == "5":
            calcular_media(alunos)
        elif opcao == "6":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida!")

# Executar o programa

main()
