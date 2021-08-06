def aplica_desconto(preco):
    preco -= preco*5 / 100
    return preco


preco = float(input('Digite o preço do produto: R$'))

print(f'O preço do produto de valor R${round(preco, 2)} fica R${round(aplica_desconto(preco), 2)}')
