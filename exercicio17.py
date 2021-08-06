from random import choice
from os import system

def sorteia(lista_de_alunos):
    return choice(lista_de_alunos)


lista_de_alunos = []

for i in range(1, 5):
    nome_aluno = str(input(f'Digite o nome do {i}º aluno: ')).capitalize().strip()

    lista_de_alunos.append(nome_aluno)

system('cls')

print('-'*40)
print(f'O aluno sorteado foi o(a) {sorteia(lista_de_alunos)}'.center(40))
print('-'*40)