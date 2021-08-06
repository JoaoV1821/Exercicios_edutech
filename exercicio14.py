def calcula_aumento(salario):
     salario += salario * 15 / 100
     return salario


salario = float(input('Digite o salário: R$'))

print(f'Salário de R${salario:.2f} com 15% de aumento: R${calcula_aumento(salario):.2f}')

