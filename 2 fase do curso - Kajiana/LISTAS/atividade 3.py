nome = input("digite seu nome por gentileza: ")
idade = int(input("digite sua idade: "))

if idade == 0 and idade < 3:
    print(f"seu filho {nome} esta destinado ao berçario!")
elif idade >= 3 and idade < 8:
    print(f"seu filho {nome} esta destinado a educação infantil!")
elif idade >= 7 and idade < 11:
    print(f"seu filho {nome} esta destinado ao fundamental nivel 1!")
elif idade >= 10 and idade < 16:
    print(f"seu filho {nome} esta destinado ao ensino fundamental 2!")
elif idade >= 16 and idade < 19:
    print(f"seu filho {nome} esta destinado ao ensino medio, parabens responsavel!!")
else: 
    print("erro")
          