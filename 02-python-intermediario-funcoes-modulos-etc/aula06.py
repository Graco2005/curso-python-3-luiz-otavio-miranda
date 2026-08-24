"""
Args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)



# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0

    for numero in args:
        total += numero
    return total


soma_1 = soma(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f'Total: {soma_1}')

numeros = 10, 20, 30, 40, 50, 60, 70, 80, 90
soma_2 = soma(*numeros) # '*' realiza o desempacotamento
print(f'Total: {soma_2}')

# Porém, no python já temos uma função de soma
soma_com_sum = sum((10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
print(f'Total usando a função sum do python: {soma_com_sum}')

# Para a função sum do python, não é necessário realizar o desempacotamento
print(sum(numeros))