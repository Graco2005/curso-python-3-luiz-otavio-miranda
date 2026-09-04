# Try, except, else e finally

try:
    a = 10
    b = 0
    c = a / b
    print('Linha 2 que não será executada')
except ZeroDivisionError as e:
    print(f'{e.__class__.__name__}: {e}')
except NameError:
    print('Alguma variável não está definida.')
except (TypeError, IndexError) as e:
    print('TypeError + indexError')
    print('Mensagem:', e)
    print('Nome:', e.__class__.__name__)
except Exception:
    print('Erro desconhecido.')

print('CONTINUANDO')