import os

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump

caminho_arquivo = '/home/luisgraco/Documents/Programing/curso-python-3-luiz-otavio-miranda'
caminho_arquivo += 'aula56.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()

# 'w' siginifica 'write', caso eu queria fazer mais funções que somente ler o arquivo eu adiciono o '+'
# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4 \n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline())

#     print('READLINES')
#     for linha in arquivo.readlines():
#         print(linha.strip())

# 'r' = read
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# 'a' significa append e junta os comandos atuais com os já existentes no arquivo
with open(caminho_arquivo, 'a+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4 \n')
    )

# os.remove(caminho_arquivo) # ou unlink
os.rename(caminho_arquivo, 'aula56-2.txt')
