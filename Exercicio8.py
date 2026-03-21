# Remover uma chave com segurança

nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))

produto = {'nome': nome, 'preco': preco}
print("---------------------------------------------------------")
print('Lista de produto:', produto)

produto.pop('desconto', None)
print("---------------------------------------------------------")
print('Lista de produto atualizado:', produto)