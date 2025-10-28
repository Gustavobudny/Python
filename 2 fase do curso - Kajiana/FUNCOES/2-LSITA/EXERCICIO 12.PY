from datetime import datetime, timedelta

agora = datetime.now()
print("Data e hora atual:", agora)

ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = datetime.now().year - ano_nascimento
print("Sua idade é:", idade)

data = datetime.now()
nova_data = data + timedelta(days=15)
print("Data atual:", data)
print("Data daqui 15 dias:", nova_data)
