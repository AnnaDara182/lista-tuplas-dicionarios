#Remova um número se ele existir

num1= int(input('Digite o primeiro número: '))
num2= int(input('Digite o segundo número: '))
num3= int(input('Digite o terceiro número: '))
num4= int(input('Digite o quarto número: '))
numeros= [num1, num2, num3, num4]
print("---------------------------------------------------------")
print('Números digitados:', numeros)
print("---------------------------------------------------------")
print("O tamanho da lista é:", len(numeros))
print("---------------------------------------------------------")

removerNum = int(input('Digite o número a ser removido: '))
print("---------------------------------------------------------")
if removerNum in numeros:
    numeros.remove(removerNum)
    print('Número removido com sucesso! Lista atualizada:', numeros)
else:
    print('Número não encontrado na lista.')
print("---------------------------------------------------------")
print("Tamanho da lista atualizado:", len(numeros))