# Manipulando chaves e valores em dicionários

pessoa = {} # Dicionário vazio

# Adicionando uma chave-valor no meu dicionário
pessoa['nome'] = 'Luis Graco'
print(pessoa)
print(pessoa['nome'])

# Caso tente acessar uma chave inexistente do dicionário, será retornado um 'KeyError'
# print(pessoa['idade'])

# Chave dinâmica

chave = 'endereço'

pessoa[chave] = 'Rua das Palmeiras'

print(pessoa[chave])

print('Antes do delete: \n', pessoa)

# Deletando uma chave do dicionário usando del
del pessoa['chave']
print()
print('Depois do delete: \n', pessoa)

# Tentando obter uma chave utilizando .get

if pessoa.get('chave') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['chave'])
