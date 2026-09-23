# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# 1a forma: Criando uma função zipper
def zipper(lista01, lista02):
    intervalo_max = min(len(lista01), len(lista02))

    return [
        (lista01[i], lista02[i]) for i in range(intervalo_max)
    ]

print(zipper(l1, l2))


# 2a forma: Usando a função 'zip' do python

print()
print(list(zip(l1, l2)))
