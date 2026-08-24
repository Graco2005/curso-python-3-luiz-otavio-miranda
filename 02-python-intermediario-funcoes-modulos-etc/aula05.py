"""
Retorno de valores das funções (return)
"""

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

# Exemplos que retornam x + y
soma1 = soma(1, 2)
soma2 = soma(5, 6)
print(soma1)
print(soma2)

# Exemplo que retorna a lista
lista = soma(11, 50)
print(lista)