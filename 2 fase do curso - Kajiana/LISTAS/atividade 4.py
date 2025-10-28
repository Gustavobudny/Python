nome = input("digite seu nome por gentileza: ")
idade = int(input("digite sua idade: "))
peso = float(input("digite seu peso em (kg) por favor: "))

if idade < 16:
    print(f"seu filho {nome} nao esta apto a ser doador de sangue")
elif idade >= 16 and idade < 18 and peso > 55:
    print(f"{nome} podera ser doador de sangue com autorização dos responsaveis!")
elif idade >= 18 and idade < 70:
    print(f"que bom {nome} pode se tornar um doador de sangue, por favor nos consulte!")
elif idade >= 69:
    print(f"desculpe senhor(a) {nome}, você não tem mais idade para doar sangue, não esta mais apto!")
else:
    print("ocorreu um erro")