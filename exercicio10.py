def tabuada(num):
    print('-'*16)
    for i in range(1, 11):
        print(f'{num} X {i} = {round(num*i, 2)}')
    print('-'*16)

num = float(input('Digite um número para ver a sua tabuada: '))

tabuada(num)