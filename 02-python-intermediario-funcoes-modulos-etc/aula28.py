# dir, hasattr e getattr em Python

string = 'Luis Graco'
metodo = 'capitalize'

if hasattr(string, metodo):
    print('EXISTE', metodo)
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)