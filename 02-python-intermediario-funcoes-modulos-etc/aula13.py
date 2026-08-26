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

pessoa = {
    'nome': 'Luis Graco',
    'sobrenome': 'Capistrano',
    'idade': 20,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

# Consultando a quantidade de endereços
# print(f'Quantidade de endereços do dicionário "pessoa": {len(pessoa)}')

# # Consultando as chaves do dicionário (keys)
# print(f'Chaves do dicionário: {pessoa.keys()}')

# lista_chaves = list(pessoa.keys())

# print(chaves[1])

# Outra forma de acessar as chaves de pessoa
# for chave in pessoa.keys():
#     print(f'Acessando chaves com for: {}')


# # Agora, vamos consultar os valores desse dicionário(values)
# print(f'Valores do dicionário: {pessoa.values()}')

# lista_valores = list(pessoa.values())

# print(f'Lista dos valores: {lista_valores}')

# # Acessando os valores com loop
# for valores in pessoa.values():
#     print(f'Acessando valores com for: {valores}')


# Acessando a chave e o valor(items)
# print(pessoa.items())

# lista_items = list(pessoa.items())

# print(lista_items)

# # Acessando chave e valor com loop
# i = 1
# for chave, valor in pessoa.items():
#     print(f'{i} - Chave: {chave}, Valor: {valor}')
#     i += 1