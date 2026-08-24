"""
Exercícios com funções

1:
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.

2:
Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

# Função 1
from math import prod

def mult(*args):
    return prod(args)

qtd = int(input('Quantos números você deseja digitar?'))

lista_numeros = []

for i in range(qtd):
    num = float(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(num)

tupla_numeros = tuple(lista_numeros)

resultado = mult(*tupla_numeros)
print(resultado)


# Função 2
# def oddOrEven(n):

#     int_n = int(n)
#     mult_dois = int_n % 2 == 0

#     if mult_dois:
#         return f'O número {n} é par.'
#     return f'O número {n} é ímpar.'

# input_usuario = input('Digite um número inteiro qualquer: ')

# print(oddOrEven(input_usuario))