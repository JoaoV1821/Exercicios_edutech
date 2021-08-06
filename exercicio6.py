from os import system

def calculo(num1, num2):
   print(f'{num1 - 1} <- {num1} -> {num1 + 1}\n{num2-1} <- {num2} -> {num2 + 1}\nSoma entre {num1} e {num2}: {num1 + num2}')


num1 = int(input('Digite um número:'))
num2 = int(input('Digite mais um número:'))

system('cls')
print('-'*20)
calculo(num1, num2)
print('-'*20)