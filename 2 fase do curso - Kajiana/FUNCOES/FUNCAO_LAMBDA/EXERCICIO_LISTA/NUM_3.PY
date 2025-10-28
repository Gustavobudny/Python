tarefas = []

adicionar = lambda ts: ts.append({"id": len(ts) + 1, "tarefa": input("Descrição: "), "status": "pendente"}) or print("Tarefa adicionada!")
visualizar = lambda ts: print("\n".join([f"ID: {t['id']} | {t['tarefa']} | {t['status']}" for t in ts]) if ts else "Nenhuma tarefa.")
atualizar = lambda ts: (next((t.update({"tarefa": input("Nova descrição: ")}) or print("✏️ Atualizada!") for t in ts if t["id"] == int(input("ID da tarefa: "))), print("ID não encontrado")))
excluir = lambda ts: (ts.pop(i) or print(" Excluída!") if (i := next((i for i, t in enumerate(ts) if t["id"] == int(input("ID da tarefa: "))), None)) is not None else print("ID não encontrado"))

def main():
    opcoes = {
        "1": lambda: adicionar(tarefas),
        "2": lambda: visualizar(tarefas),
        "3": lambda: atualizar(tarefas),
        "4": lambda: excluir(tarefas),
        "5": lambda: exit("BYEE BYEE")
    }

    while True:
        print("\nSistema de Tarefas")
        print("1. Adicionar | 2. Visualizar | 3. Atualizar | 4. Excluir | 5. Sair")
        opcoes.get(input("Escolha: "), lambda: print("Opção inválida!"))()

main()
