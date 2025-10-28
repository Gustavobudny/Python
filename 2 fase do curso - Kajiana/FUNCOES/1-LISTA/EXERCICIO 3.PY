def imprimir_funcionario(nome, salario = 9000):
    print(f"Nome do funcionário: {nome}")
    print(f"Salário: R$ {salario:.2f}")

nome = input("Digite o seu nome: ")
salario_input = input("Digite o seu salario: ")

if salario_input.strip() == "":
    imprimir_funcionario(nome)
else:
    imprimir_funcionario(nome, float(salario_input))
          
