notas = {"ana": [7, 8, 9], "marcos": [6, 5, 7]}

for alunos,nota in notas.items():
    media = (nota[0] + nota[1] + nota[2]) / 3
    if media >= 7:
        print(media)