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

p1 = {
    'nome': 'Luis Graco',
    'sobrenome': 'Capistrano',
}

print(p1)

# print(p1.get('nome'))
# print(p1.get('nome', 'Não existe nome')) # Caso não exista a chave 'nome', o segundo parâmetro da função é executado

# Apaga e retorna o valor indicado na chave
# nome = p1.pop('nome')
# print(f'Valor retornado da função pop: {nome}')
# print(p1)

# Elminando a última chave com a função popitem
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(f'Chave retornada da função popitem: {ultima_chave[0]}')
# print(f'Valor retornado da função popitem: {ultima_chave[1]}')
# print(p1)

# Atualizando, adicionando, alterando o meu dicionário de forma dinâmica com a função update
# p1.update({
#     'nome': 'Pedro Costa',
#     'idade': 24
# })
# print(f'Primeiro update: {p1}')

# # Também consigo usar o update passando argumentos nomeados dentro da função
# p1.update(nome='Luis Graco', idade=20)
# print(f'Segundo update passando argumentos nomeados para a função: {p1}')

# Por fim, também é possível utilizar a função update através de uma tupla/lista
tupla = ('chave', 'valor da chave'), ('idade', 35), ('nome', 'Paulo Neves')
p1.update(tupla)
print(p1)