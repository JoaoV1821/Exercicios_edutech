valor = input('Digite alguma coisa: ')

if valor.isalnum():
    print(f'O valor "{valor}" é alfanumérico')

if valor.isalpha():
    print(f'O valor "{valor}" é alfabético')

if valor.isdecimal():
    print(f'O valor "{valor}" é decimal')

if valor.isdigit():
    print(f'O valor "{valor}" é dígito')

if valor.isidentifier():
    print(f'O valor "{valor}" é identifier')

if valor.isnumeric():
    print(f' valor "{valor}" é numérico')

if valor.islower():
    print(f'O valor "{valor}" é minúsculo')

if valor.isupper():
    print(f'O valor "{valor}" é maiúsculo')

if valor.isspace():
    print(f'O valor "{valor}" tem espaços')

if valor.istitle():
    print(f'O valor "{valor}" tem formataçã de título')

if valor.isascii():
    print(f'O valor "{valor}" está na tabela ASCII')



funcoes = {
    valor.isalnum(): 'O valor é alfanumérico',
    valor.istitle(): 'O valor tem formatação de título'
}

for k,v in funcoes:
    if valor:
        print(k,v)
