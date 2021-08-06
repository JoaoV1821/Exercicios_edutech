from os import system

def calcula_orcamento(km, dias):
    preco_por_dia = dias * 60
    preco_por_km = km * 0.15

    return preco_por_dia + preco_por_km


dias = int(input('Por quantos dias o carro foi alugado ?: '))

km = float(input('Quantos quilômetros foram rodados com o carro ?: '))

system('cls')

print('-'*40)
print(f'O orçamento final será de R${calcula_orcamento(km, dias):.2f}'.center(40))
print('-'*40)