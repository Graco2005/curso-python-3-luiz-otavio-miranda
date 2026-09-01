# isisntance - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), 
    {0, 1}, {'nome': 'Luis'}
]

# Tem como uma de suas funcionalidades filtrar tipos vindo de uma lista
for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print('->', item, isinstance(item, set))

    # Printado primeiro pois o 'a' vem primeiro na lista
    elif isinstance(item, str):
            print('STRING')
            print('->', item.upper())

    # Usando "ou" - ou int ou float
    elif isinstance(item, (int, float)):
         print('NUM')
         print(item, '->', item * 2)

    # Caso default
    else:
         print('OUTRO')
         print('->', item)