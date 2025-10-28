import tkinter as tk

#funcao que sera executada pelo botao
def saudacao():
    nome = entrada_nome.get() #pega o nome digitado no campo de entrada e passa pra variavel nome
    if nome.strip(): #verifica se o nome n esta vazio
        mensagem.config(text = f"Ola, {nome}!, seja bem vindo ao mundo python.")
    else:
        mensagem.config(text = "Digite seu nome antes de começar.")


janela = tk.Tk() #cria a janela principal de aplicação
janela.title("Gerador de boas vindas!") #adiciona titulo na janela
janela.geometry("400x250") #da um tamanho pra esta janela (largura  x altura)
imagem = tk.PhotoImage(file="")

rotulo = tk.Label(janela, text = "Digite seu nome por favor.", font=("Arial", 12)) #rotulo explicativo

titulo = tk.Label(janela, text = "Interface Grafica com Python :>", font=("Arial", 16, "bold")) #titulo da aplicação mostrado pro usuario
titulo.pack(pady = 10) #adiciona margem superior (pack = organiza a janela, pady = adiciona margem)

entrada_nome = tk.Entry(janela, font=("Arial", 12), justify = "center") #campo de entrada do texto
entrada_nome.pack(pady = 5)

botao = tk.Button(janela, text = "Gerar mesnagem", font=("Arial", 12, "bold"), bg = "#4CAF50", fg = "white", command= saudacao) #criacao do botao, command = nome da funcao ora chamar o botao
botao.pack(pady = 10)

mensagem = tk.Label(janela, font=("Arial", 12), fg = "blue")#rotulo pra exebir a mensagem de boas-vindas
mensagem.pack(pady = 10)

janela.mainloop()#iniciar o loop da aplicação