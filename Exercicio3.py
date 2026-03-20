# Atualizar elemento com uma operação

num1= int(input('Digite o primeiro número: '))
num2= int(input('Digite o segundo número: '))
num3= int(input('Digite o terceiro número: '))
numeros= [num1, num2, num3]
print("---------------------------------------------------------")
print('Números digitados:', numeros)

numeros[2]= num1 + num2
print("---------------------------------------------------------")  
print('Lista atualizada com a soma do primeiro e segundo número:', numeros)