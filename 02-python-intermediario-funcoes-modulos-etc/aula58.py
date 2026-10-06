# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('Luis')
adiciona_clientes('Marina', cliente1)
adiciona_clientes('Vinícius', cliente1)
cliente1.append('José')
print(cliente1)

cliente2 = adiciona_clientes('Guilherme')
adiciona_clientes('Juan', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Alan')
adiciona_clientes('Gleison', cliente3)
print(cliente3)
