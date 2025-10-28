def medias (a, b, c):
    media = (a + b + c)/3
    return media
    
def analise ():
    if media > 6:
        print("Parabens você foi aprovado!")
    elif media > 4 and media < 6:
        print("Você esta em recuperação, melhor estudar!")
    elif media < 4:
        print("Você rodou!")
    else:
        print("Funfou não pai")

a = float(input("Digite sua nota 1: "))
b = float(input("Digite sua nota 2: "))
c = float(input("Digite sua nota 3: "))

media = medias(a, b, c)
print(f"a sua media sera: {media}")
analise()