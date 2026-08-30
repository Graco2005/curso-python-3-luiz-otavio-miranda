# Empacotamento e desempacotamento de dicionários
a, b, = 1, 2
a, b = b, a

# print(a, b)

pessoa = {
    'nome': 'Ana Maria',
    'sobrenome': 'Farias Abreu'
}

# Formas de desempacotar um dicionario
# a, b = pessoa.items()
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')

dados_pessoa = {
    'idade': 46,
    'altura': 1.54,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

# for chave, valor in pessoa_completa.items():
#     print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    print('NOMEADOS:')
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

# Empacotamento
# mostrar_argumentos_nomeados(1, 'oi', 'argumento não nomeado', True, nome='Joana', qualquer=123)

# Desempacotamento
# mostrar_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostrar_argumentos_nomeados(**configuracoes)