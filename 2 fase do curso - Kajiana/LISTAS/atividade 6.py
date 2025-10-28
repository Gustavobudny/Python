nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

if idade <= 15:
    print(f"senhor {nome} voce nao pode votar ainda")
elif idade >= 18 and idade < 66:
    print(f"seu voto e obrigatorio, pro favor fique atento aos dias de votar")
elif idade == 16 or idade == 17 or idade < 65:
    print("seu voto e opcional, vote com consciencia!")
else:
    print("ocorreu algum erro, tente novamente!")