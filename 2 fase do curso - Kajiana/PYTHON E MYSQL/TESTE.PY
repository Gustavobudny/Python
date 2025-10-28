import tkinter as tk
import random
from tkinter import messagebox #abre janela pop-up

#funcao principal do jogo
def jogar(escolha_jogador):
    opcoes =["pedra", "papel","tesoura"]
    escolha_computador = random.choice(opcoes)

    #exibe o que cada um escolheu
    label_resultado.config(text = f"Voce escolheu: {escolha_jogador}\n O computador escolheu: {escolha_computador}")

    #verificar vencedor
    if escolha_jogador == escolha_computador:
        resultado = "empate!"
    elif ((escolha_jogador == "pedra" and escolha_computador == "tesoura") or (escolha_jogador == "tesoura" and escolha_computador == "papel") or (escolha_jogador == "papel" and escolha_computador == "pedra")):
        resultado = "Você venceu"
    else:
        resultado = "Você perdeu e o computador venceu"
    
    #mostrar resultado
    messagebox.showinfo("resultado", resultado)

#criacao da janela

janela = tk.Tk()
janela.title("Jokenpo hehehe")
janela.geometry("500x300")
janela.config(bg="#f0f0f0")

#Ttitulo principal
titulo =tk.Label(janela, text = "jokenpo pythonico", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady = 10)

#instrucao do jogo
instrucao = tk.Label(janela, text = "Escolha uma das opcoes abaixo", font=("Arial", 12), bg = "#f0f0f0")
instrucao.pack()

#botoes de escolha do jogador
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(pady = 10)

botao_pedra = tk.Button(frame_botoes, text  = "pedra", font=("Arial", 12, "bold"), width=10, command=lambda:jogar("pedra"))
botao_pedra.grid(row = 0, column = 0, padx = 5)

botao_papel = tk.Button(frame_botoes, text  = "papel", font=("Arial", 12, "bold"), width=10, command=lambda:jogar("papel"))
botao_papel.grid(row = 0, column = 1, padx = 5)

botao_tesoura = tk.Button(frame_botoes, text  = "tesoura", font=("Arial", 12, "bold"), width=10, command=lambda:jogar("tesoura"))
botao_tesoura.grid(row = 0, column = 2, padx = 5)

#rrotulo para mostrar as escolhas
label_resultado = tk.Label(janela, text = "Faça sua escolha pra começar o jogo", font=("Arial", 12), bg = "#f0f0f0", fg = "blue")
label_resultado.pack(pady = 20)

#abrir a janela
janela.mainloop()
