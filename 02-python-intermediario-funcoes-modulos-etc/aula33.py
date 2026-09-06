# try, except, else e finally

# Graças ao finally, o bloco de código dentro dele sempre será executado mesmo se houver algum erro no try
try:
    print('ABRINDO ARQUIVO')
    # Erro de zero division
    8 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO')
except IndexError as e:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHANDO ARQUIVO')