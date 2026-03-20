# Notas: subtituir a menor nota, ordenar e recalcular a média

nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
nota3= float(input('Digite a terceira nota: '))
notas= [nota1, nota2, nota3]
print("---------------------------------------------------------")
print('Notas digitadas:', notas)

media= sum(notas)/len(notas)
print("---------------------------------------------------------")
print('Média das notas:', media)
print("---------------------------------------------------------")

menorNota= min(notas)
novaNota= float(input('Digite a nova nota para substituir a menor nota: '))
notas.remove(menorNota)
notas.append(novaNota)
notas.sort()
print("---------------------------------------------------------")
print('Notas atualizadas e ordenadas:', notas)
novaMedia= sum(notas)/len(notas)
print("---------------------------------------------------------")
print('Nova média das notas:', novaMedia)