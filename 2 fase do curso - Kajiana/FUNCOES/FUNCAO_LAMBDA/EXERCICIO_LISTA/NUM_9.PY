import math

#letra a

numero = float(input("digite seu numero: "))
raiz = (lambda x: math.sqrt(x))(numero)
print(f"a raiz de {numero} sera de: {raiz:.2f}")

#letra b

angulo = float(input("digite um angulo em graus: "))
seno = (lambda x: math.sin(math.radians(x)))(angulo)
print(f"O seno de {angulo}° é {seno:.4f}")

#letra c

numero = float(input("digite um numero decimal: "))

arredondado = list(map(lambda func: func(numero), [math.ceil, math.floor]))

print(f"numero original: {numero}")
print(f"arredondado para cima (ceil): {arredondado[0]}")
print(f"arredondado para baixo (floor): {arredondado[1]}")