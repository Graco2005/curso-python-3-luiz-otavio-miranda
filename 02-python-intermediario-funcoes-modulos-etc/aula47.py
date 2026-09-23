"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Solução Bruta (com função)
def somar_duas_listas(lista01, lista02):

    intervalor_menor_lista = min(len(lista01), len(lista02))
    nova_lista = []
    for i in range(intervalor_menor_lista):
        nova_lista.append(lista01[i] + lista02[i])

    return nova_lista

print(somar_duas_listas(lista_a, lista_b))

# Solução vídeo
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)