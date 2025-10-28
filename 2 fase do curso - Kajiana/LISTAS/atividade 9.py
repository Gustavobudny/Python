lista_m = []
lista_f = []
lista_total = []


for i in range (4):
    sexo = input("digite seu sexo: M ou F:   ").lower()
    if sexo == "m":
        altura = float(input("digite sua altura pro favor: "))
        lista_m.append(altura)
        lista_total.append(altura)
    elif sexo == "f":
        altura = float(input("digite sua altura pro favor: "))
        lista_f.append(altura)
        lista_total.append(altura)
    else:
        print("ocorreu um erro")

print("o maximo do feminino sera de: ",max(lista_f))
print("o maximo do masculino sera de: ", max(lista_m))

soma = sum(lista_f)
media = soma / len(lista_f)

print(f"a media da altura das mulheres sera de: {media}")
print("o numero de homens sera de: ",len(lista_m))

porcen_m = (len(lista_m) / len(lista_total)) * 100
porcen_f = (len(lista_f) / len(lista_total)) * 100

print(f'a porcentagem de homens sera de: {porcen_m}%, e a porcentagem de mulheres sera de {porcen_f}% ')




