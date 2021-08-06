from random import choice
from os import system

def calcula_porcentagem(valor, taxa):
    valor += valor * taxa/100
    return valor


lista_de_funcionarios = {}

for i in range(1, 11):
    nome_funcionario = str(input('Digite o nome do funcionário: '))
    salario_do_funcionario = float(input('Digite o salário do funcionario: '))

    lista_de_funcionarios[nome_funcionario] = salario_do_funcionario

    if i % 3 == 0: 
        for k,v in lista_de_funcionarios.items():
            lista_de_funcionarios[k] = round(calcula_porcentagem(v, 5), 2)      

    
system('cls')

print('-'*75)
print(' '*75)

for k,v in lista_de_funcionarios.items():
    print(f'Funcionário: {k:>4} - Salário: R${v:.2f}\n')

funcionarios_nomes = []

for nome in lista_de_funcionarios.keys():
    funcionarios_nomes.append(nome)

nome_sorteado = choice(funcionarios_nomes)

lista_de_funcionarios[nome_sorteado] = round(calcula_porcentagem(lista_de_funcionarios[nome_sorteado], 10), 2)

print('-'*75)
print(f'O funcionário sorteado para ganhar 10% de aumento foi o(a) {nome_sorteado}\nSalário novo: R${lista_de_funcionarios[nome_sorteado]:.2f}'.center(60))
print('-'*75)
