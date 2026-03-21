# Acessar elementos da tupla

fruta1= str(input('Digite o nome da fruta 1: '))
fruta2= str(input('Digite o nome da fruta 2: '))
fruta3= str(input('Digite o nome da fruta 3: '))
frutas= (fruta1, fruta2, fruta3)
print("---------------------------------------------------------")
print('Frutas: ', frutas)
print("---------------------------------------------------------")

buscar = input('Digite uma fruta para verificar: ')
if buscar in frutas:
    print("---------------------------------------------------------")
    print(f'A fruta {buscar} está presente na tupla.')
else:
    print("---------------------------------------------------------")
    print(f'A fruta {buscar} não está presente na tupla.')