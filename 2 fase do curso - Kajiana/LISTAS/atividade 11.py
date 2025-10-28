cidades = ["Criciuma", "Içara", "Sideropolis", "Urussanga", "Rincão"]
acidentes = [120, 80, 55, 75, 30]
veiculos = [9500, 3000, 2100, 2800, 1700]

maior_indice = max(acidentes)
menor_indice = min(acidentes)
cidade_maior = cidades[acidentes.index(maior_indice)]
cidade_menor = cidades[acidentes.index(menor_indice)]

print(f'maior indice de acidentes: {maior_indice} em {cidade_maior}')
print(f"a menor indice de acidentes: {menor_indice} em {cidade_menor}")

media_veiculos = sum(veiculos) / len(veiculos)
print(f"a media de veiculos sera de {media_veiculos}")

acidentes_menor = [acidentes[i] for i in range(5) if veiculos[i] < 2000]

if acidentes_menor:
    media_acidentes_menor = sum(acidentes_menor) / len(acidentes_menor)
    print(f"a media de acidentes nas cidades com menos de 2000 veiculos sera de {media_acidentes_menor:.2f}")
else:
    print("nenhuma cidade possui menos de 2000 veiculos de passeio")



