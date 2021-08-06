def converte_para_dolar(valor_em_reais):
    DOLAR = 5.30
    valor_convertido = valor_em_reais*DOLAR
    valor_a_ser_comprado = valor_em_reais/DOLAR

    return f'Valor convertido em dólares: ${round(valor_convertido, 2)}\nPoderá ser comprado: ${round(valor_a_ser_comprado, 2)}'


quantia = float(input('Valor em reais: R$'))

print(converte_para_dolar(quantia))
