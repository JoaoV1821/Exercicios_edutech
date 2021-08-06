from os import system

def converte_fahrenheit(celsius):
    convertido = 9 * celsius / 5 + 32
    return convertido


temperatura = float(input('Digite uma temperatura em °C: '))

system('cls')

print('-'*20)
print(f'{temperatura:.2f}°C = {converte_fahrenheit(temperatura):.2f}°F')
print('-'*20)