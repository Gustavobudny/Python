nome = input('digite seu nome por favor: ')
idade = int(input('digite sua idade por gentileza: '))
valorp = float(input('digite o seu valor do plano: '))

if idade < 0:
    print('erro, idade invalida')
elif idade >=0 and idade < 19:
    aumento = valorp + (valorp * 5/100)
    print(f'o seu salario sera de: {aumento}')
elif idade > 18 and idade < 36:
    aumento = valorp + (valorp * 10/100)
    print(f'o seu salario sera de: {aumento}')
elif idade > 35 and idade < 61:
    aumento = valorp + (valorp * 15/100)
    print(f'o seu salario sera de: {aumento}')
elif idade > 60:
    aumento = valorp + (valorp * 20/100)
    print(f'o seu salario sera de: {aumento}')
else:
    print('erro, tente novamente')
