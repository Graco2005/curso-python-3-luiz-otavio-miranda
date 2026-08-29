# Função de apoio para executar as outras funções
def executa(funcao, *args):
    return(funcao(*args))


# def soma(x, y):
#     return x + y


# def criar_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# Usando a função lambda para substituir a função soma
print(
    executa(lambda x, y: x + y, 2, 3)
)

# A modo de comparação, aqui estão as outras formas de executar essa função de soma, gerando sempre o mesmo resultado
# print(executa(soma, 2, 3), end=' ')
# print(soma(2, 3))


# Usando lambda para simplificar a função def criar_multiplicador e def multiplica
duplica = executa(lambda m: lambda n: m * n, 2)
print(duplica(2))


print(
    executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6)
)
