def converte(metragem):
    cm = metragem*100
    mm = metragem*1000

    print(f'Cm: {cm}cm\nMm: {mm}mm')


metragem = float(input('Digite um valor em Metros: '))

converte(metragem)