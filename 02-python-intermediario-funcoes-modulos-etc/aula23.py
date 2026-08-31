# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)

# print(lista)

# Aplicando list comprehension
lista = [
    numero * 2
    for numero in range(10)
]

# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')

# p(novos_produtos)

# List comprehension + if ternário
# lista = list(n for n in range(10) if n < 5)

# O que vem a esquerda do for é mapeamento, o que vem a direita do for é filtro
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] * 1.05) >= 20 and produto['preco'] * 1.05 > 10
]
p(novos_produtos)
