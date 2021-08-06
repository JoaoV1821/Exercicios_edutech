nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
data_de_nascimento = str(input('Digite sua data de nascimento (no formato DDMMAAA): '))

print(f'Seu nome é {nome}\nSua idade é {idade}\nSua data de nascimento é {data_de_nascimento[0:2]}/{data_de_nascimento[2:4]}/{data_de_nascimento[4:]}')
