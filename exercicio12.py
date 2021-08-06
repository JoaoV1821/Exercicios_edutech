from os import system

def calcula_medidas(altura, largura):
    area = altura * largura
    tinta_necessaria = area / 2

    return f'Área total: {round(area,2)}m²\nTinta necessária para pintar a parede: {round(tinta_necessaria)}L'


altura = float(input('Digite a altura da parede em metros:'))

largura = float(input('Digite a largura da parede em metros: '))

system('cls')
print('-'*42)
print(calcula_medidas(altura, largura))
print('-'*42)
