# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

# O iterator(iterator) não sabe nada do iterável(iterable), ele só sabe entregar o próximo valor
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
