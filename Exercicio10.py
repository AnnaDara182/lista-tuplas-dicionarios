# Agenda (CRUD simples) com ordenação de nomes

agenda = {'Ana': '1111-1111', 'Bruno': '2222-2222'}
print("---------------------------------------------------------")
print('Agenda inicial:', agenda)
print("---------------------------------------------------------")

#Adicionar novo contato
novo_nome = input('Digite o nome do contato: ')
novo_telefone = input('Digite o telefone do contato: ')
agenda[novo_nome] = novo_telefone

print("---------------------------------------------------------")
print('Agenda atualizada:', agenda)
print("---------------------------------------------------------")

# Atualizar telefone de um contato existente
atualizar_nome = input('Digite o nome do contato a atualizar: ')
if atualizar_nome in agenda:
    novo_telefone = input(f'Digite o novo telefone: ')
    agenda[atualizar_nome] = novo_telefone
    print("---------------------------------------------------------")
    print(f'Telefone de {atualizar_nome} atualizado.')
    print("---------------------------------------------------------")
else:
    print("---------------------------------------------------------")
    print(f'Contato não encontrado.')
    print("---------------------------------------------------------")

print('Após possível atualização:', agenda)
print("---------------------------------------------------------")

# Remover um contato
remover_nome = input('Digite o nome do contato a remover: ')
if remover_nome in agenda:
    del agenda[remover_nome]
    print("---------------------------------------------------------")
    print(f'Contato {remover_nome} removido.')
    print("---------------------------------------------------------")
else:
    print("---------------------------------------------------------")
    print("Contato não encontrado.")
    print("---------------------------------------------------------")

print('Após possível atualização:', agenda)
print("---------------------------------------------------------")


#Exibir contatos ordenados
print("Contatos em ordem alfabética:")
for nome in sorted(agenda.keys()):
    print(nome, ":", agenda[nome])