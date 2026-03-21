# Exibir maior e menor valor

num1= int(input('Digite um número: '))
num2= int(input('Digite outro número: '))
num3= int(input('Digite mais um número: '))
num4= int(input('Digite o último número: '))
numeros= (num1, num2, num3, num4)

print("---------------------------------------------------------")
print('Números: ', numeros)
print("---------------------------------------------------------")
print(f'O maior número é: {max(numeros)}')
print("---------------------------------------------------------")
print(f'O menor número é: {min(numeros)}')