votantes = int(input("digite a quantidade total de votantes: "))

op_1 = 0
op_2 = 0
op_3 = 0

for i in  range (votantes):
    print("escolha um dos candidatos\n" \
    "digite 1 para candidato 1,\n" \
    "digite 2 para candidato 2\n" \
    "digite 3 para candidato 3")
    op = (input("escolha um dos candidatos: "))

    match op: 
        case "1":
            op_1 += 1
        case "2":
            op_2 += 1
        case "3":
            op_3 += 1

print(f"o candidatoo 1 teve {op_1} votos\no candidato 2 teve {op_2} votos\no candidato 3 teve {op_3} votos ")
