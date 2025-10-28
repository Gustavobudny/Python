meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
templista = []

a = 1

for i in range(12):
    temp = int(input(f'digite a temperatura do mes {a}: '))
    templista.append(temp)
    a += 1

media = sum(templista) / len(templista)

print(f'a media de temperatura anual foi de: {media}')

for b in templista:
    if b > media:
        print(b)

