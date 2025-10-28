nome = input("digite seu nome: ")
peso = float(input("digite sseu peso: "))
altura = float(input("digite sua altura: "))

IMC = peso / (altura * altura)

print(f"seu IMC e de: {IMC}")

if IMC <= 18.4:
    print("voce esta abaixo do peso!")
elif IMC >= 18.5 and IMC <= 25:
    print("voce esta com o peso normal!, que bommm")
elif IMC > 25 and IMC <= 30:
    print("voce esta acima do peso, cuide se!")
elif IMC > 30:
    print("voce esta imenso pai, vamo se cuidar ne gordao da xj6")
else:
    print("algo deu errado, tente novamente")