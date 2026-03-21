# ontar quantas vezes um número aparece

num1= int(input('Digite um número: '))
num2= int(input('Digite outro número: '))
num3= int(input('Digite mais um número: '))
num4= int(input('Digite o último número: '))
numeros= (num1, num2, num3, num4)
print("---------------------------------------------------------")
print('Números: ', numeros)
print("---------------------------------------------------------")
buscar= int(input('Digite um número para verificar: '))
contador= numeros.count(buscar)
print("---------------------------------------------------------")
print(f'O número {buscar} aparece {contador} vezes na tupla.')