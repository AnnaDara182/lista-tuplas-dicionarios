# Atualizar preço e quantidade; calcular o total 

nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))

produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}

aumento = float(input('Digite o aumento percentual do preço (ex: 10 para 10%): '))

produto['preco'] = produto['preco'] * (1 + aumento / 100)

produto['quantidade'] = produto['quantidade'] + 2

total = produto['preco'] * produto['quantidade']
print("---------------------------------------------------------")
print('Produto atualizado:', produto)
print("---------------------------------------------------------")
print('Total (preço x quantidade):', total)