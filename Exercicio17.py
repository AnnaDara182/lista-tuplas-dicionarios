# Organizar valores sem mexer na tupla original

num1= int(input('Digite o primeiro número: '))
num2= int(input('Digite o segundo número: '))
num3= int(input('Digite o terceiro número: '))
num4= int(input('Digite o quarto número: '))
numeros = (num1, num2, num3, num4)
print('----------------------------------------')
print('Números: ', numeros)
print('----------------------------------------')
print(f'Números em ordem crescente: {sorted(numeros)} | Tipo: {type(numeros)}')