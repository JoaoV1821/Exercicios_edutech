def calcula_media(nota1, nota2):
    return (nota1 + nota2) / 2


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = calcula_media(nota1, nota2)

print(f'Média: {media}')
