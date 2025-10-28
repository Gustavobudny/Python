nome_p = input("digite o nome do produto: ")
quantidade = int(input("digite a quantidade do produto: "))
preço = float(input("digite o preço deste produto: "))

print("escolha uma das opções de pagamento," \
"\n 1  a vista em dubgeiro recebe 10% de desconto" \
"\n 2  a vista no cartao de credito, recebe 5% de desconto" \
"\n 3  em duas vezes, preço normal sem desconto" \
"\n 4  em tres vezes, preço normal mais juros de 5% acrescimo")

opcao = input("digite sua opção: ")

if opcao == "1":
    RS = quantidade * preço + (quantidade * preço * 10/100)
    print(f"o pagamento saira = {RS:.2f}")
elif opcao == "2":
    RS = quantidade * preço + (quantidade * preço * 10/100)
    print(f"o pagamento saira = {RS:.2f}")
elif opcao == "3":
    RS = quantidade * preço
    print(f"o pagamento saira = {RS:.2f}")
elif opcao == "4":
    RS = quantidade * preço - (quantidade * preço * 5/100)
    print(f"o pagamento saira = {RS:.2f}")
else:
    print("ocorreu um erro tente novamente")
