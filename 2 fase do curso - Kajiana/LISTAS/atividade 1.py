ganho_hora = float(input('quantos voce ganha por hora trabalhando?:  '))
horas = int(input('quantas hotas voce trabalha no mes?: '))

bruto = horas * ganho_hora
inss = bruto * 11/100
ir = bruto * 8/100
sindicato = bruto * 5/100
descontos = inss + sindicato + ir
sl = bruto - descontos

print(f'seu salario bruto sera de: {bruto}')
print(f'seu salario liquuido sera de: {sl}')
print(f'o desconto dado pelo seu salario sera de: {descontos}') 

