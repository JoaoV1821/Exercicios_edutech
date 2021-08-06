# 341-7 |(número entre 1000 e 10000)(data do boleto)00000000(valor do boleto)

from random import randint
from os import system
from time import sleep

def formata_boleto(numero_aleatorio, data_do_boleto, valor_do_boleto):
        return f'341-7 | {numero_aleatorio}{data_do_boleto}00000000{valor_do_boleto:.0f}'


valor_do_boleto = float(input('Digite o valor do boleto: R$'))
data_do_boleto = int(input('Data do boleto no (formato DDMMAAA): '))

numero_aleatorio = randint(1000, 10000)

system('cls')
print('Gerando boleto...')
sleep(1.0)
system('cls')

print(formata_boleto(numero_aleatorio, data_do_boleto, valor_do_boleto))
