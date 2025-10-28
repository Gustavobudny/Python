gasolina = 5.65
álcool = 4.22

litros = float(input("quantos litros voce deseja adicionar a nave?: "))
tipo_g = input("qual combustivel?, A-alcool, G-gasolina: ")

if tipo_g == "A":

    if litros <= 20:
        valor = litros * álcool - (litros * álcool * 3/100)
        print(f"o valor a ser pago para {litros} de álcool, sera de: {valor}")
    elif litros > 20:
        valor = litros * álcool - (litros * álcool * 5/100)
        print(f"o valor a ser pago para {litros} de álcool, sera de: {valor}")

elif tipo_g == "G":

    if litros <= 20:
        valor = litros * gasolina - (litros * gasolina * 4/100)
        print(f"o valor a ser pago para {litros} de gasolina, sera de: {valor}")
    elif litros > 20:
        valor = litros * gasolina - (litros * gasolina * 6/100)
        print(f"o valor a ser pago para {litros} de gasolina, sera de: {valor}")
else:
    print('algo de estranho ocorreu, nao funfou!')

