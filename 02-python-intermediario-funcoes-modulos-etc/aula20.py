# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# lista = [4, 32, 1, 34, 5, 6, 6, 21]
# lista.sort(reverse=True)

# print(lista)

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# A função lambda tem a funcionalidade de encurtar e simplificar o código, substituindo a necessidade de uma função com def
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

exibir(l1)
exibir(l2)