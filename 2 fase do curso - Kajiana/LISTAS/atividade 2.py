C = float(input('digite seu valor em graus celsius: '))
print("escolha uma das opções de conversão: A) Fahrenheit B) kelvin C) réaumur: ")
opcao = input(" ")

if opcao == "A":
    F = C * 1.8 + 32
    print(f"sua conversão ficara: {F}")
elif opcao == "B":
    K = C + 273.15
    print(f"sua conversão ficara: {K}")
elif opcao == "C":
    R = C * 0.8
    print(f"sua conversão ficara: {R}")
else:
    print("ocorreu um erro, tente novamente!!")
