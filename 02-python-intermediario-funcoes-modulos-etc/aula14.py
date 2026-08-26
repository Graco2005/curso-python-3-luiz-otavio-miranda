# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave, caso a chave não existir retorna None
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

d1 = {
    'c1': 1,
    'c2': 2,
}
# Como os dicionário são dados mutáveis, o trecho de código não representa uma cópia, mas sim que as duas variáveis apontam para o mesmo endereço de memória (mesmo valor)
# d2 = d1

# # Então, se eu alterar/remover uma chave da variável d2, d1 também será afetado pois são os mesmos
# d2['c1'] = 100

# print(f'Valor de d1 alterado por d2: {d1}')

# Porém, usando a função copy eu consigo criar uma cópia de d1 em d2
# d2 = d1.copy()

# d2['c1'] = 100; d2['c2'] = 200
# print(f'Valor de d1: {d1}')
# print(f'Valor de d2: {d2}')

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2]
# }

# d2 = d1.copy()

# # Porém, isso que vimos acima não se aplica para listas, já que a função copy é uma cópia rasa e não afeta as listas
# d2['c1'] = 1000
# d2['l1'][1] = 9999

# # Mesmo após mudar a lista de d2, que é uma cópia de d1, na posição 1 o d1 também é afetado por essa troca
# print(f'Valor de d1: {d1}')
# print(f'Valor de d2: {d2}')


# Afim de resolver isso, podemos importar uma biblioteca chamada copy para fazer uma cópia longa
import copy


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 9999

# Perceba que os valores de d1 permanecem os mesmo, sendo mantida a integritade de d1 após a alteração em d2
print(f'Valor de d1: {d1}')
print(f'Valor de d2: {d2}')