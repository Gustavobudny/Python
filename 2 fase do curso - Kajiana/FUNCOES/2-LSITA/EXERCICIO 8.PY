import random

def exercicio7():
    segredo = random.randint(1, 100)
    tentativas = 0
    print(" Bem-vindo ao jogo da adivinhação!")
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        if palpite == segredo:
            print(f" Parabéns! Você acertou em {tentativas} tentativas!")
            break
        elif palpite < segredo:
            print("O número é maior!")
        else:
            print("O número é menor!")

exercicio7()