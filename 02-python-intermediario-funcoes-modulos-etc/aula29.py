# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__


# O iterator(iterator) não sabe nada do iterável(iterable), ele só sabe entregar o próximo valor
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


lista= [n for n in range(10000)]
generator = (n for n in range(100000))

# A lista armazena todos os valores na memória, enquanto o generator gera um valor por vez.
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

# Navegação sequencial
# for i in generator:
#     print(i)