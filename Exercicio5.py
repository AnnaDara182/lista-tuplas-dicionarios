# Fila: chegadas, prioridade e atendimento

fila =["Anna", "Bruno"]
print(f"Fila inicial: {fila}")
print("---------------------------------------------------------")

proxCliente1 = input("Digite o nome do próximo cliente: ")
proxCliente2 = input("Digite o nome do próximo cliente: ")
fila.extend([proxCliente1, proxCliente2])
print("---------------------------------------------------------")
print(f"Fila atualizada: {fila}")
print("---------------------------------------------------------")

prioridade= input("Digite o nome do cliente com prioridade: ")
fila.insert(0, prioridade)
print("---------------------------------------------------------")
print(f"Fila com prioridade: {fila}")
print("---------------------------------------------------------")

atendido= fila.pop(0)
print(f"Cliente atendido: {atendido}")
print("---------------------------------------------------------")
print(f"Lista atualizada: {fila}")