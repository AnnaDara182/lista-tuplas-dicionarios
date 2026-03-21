# Criar e exibir dicionário de aluno

nome= input('Digite o nome do aluno: ')
idade= int(input('Digite a idade do aluno: '))

alunos= {'nome': nome, 'idade': idade}
print("---------------------------------------------------------")
print(f'Aluno: {alunos} | Tipo: {type(alunos)}')