def valorPagamento(prestacao, dias_atraso):
    if dias_atraso == 0:
        return prestacao
    else:
        multa = prestacao * 0.03
        juros = prestacao * 0.001 * dias_atraso
        return prestacao + multa + juros

def programa_pagamentos():
    total_dia = 0
    quantidade = 0

    while True:
        prestacao = float(input("\nDigite o valor da prestação (0 para encerrar): "))
        if prestacao == 0:
            break
        dias_atraso = int(input("Digite o número de dias em atraso: "))
        valor = valorPagamento(prestacao, dias_atraso)
        print(f"Valor a ser pago: R$ {valor:.2f}")
        total_dia += valor
        quantidade += 1

    print("\n===== RELATÓRIO DO DIA =====")
    print(f"Quantidade de prestações pagas: {quantidade}")
    print(f"Valor total recebido: R$ {total_dia:.2f}")

programa_pagamentos()