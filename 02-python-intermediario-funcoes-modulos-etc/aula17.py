# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.
# Tuplas -> (); Lista -> []; sets -> {}

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set('Luis')
s1 = set() # set vazio
s1 = {'Luis', 1, 2, 3} # set co dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = {1, 2, 3, 3, 3, 3, 3, 1, 1}
# print(s1) # Reorganiza os valores e exclui os repetidos
# # Com isso em mente, podemos usar a correção de tipo para eliminar valores repetidos de listas e tuplas
# l1 = [1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 1, 2, 3] # Lista com valores bagunçados e repetidos
# s1 = set(l1) # Convertendo de lista para set
# print(s1)

# l2 = list(s1) # Convertendo de volta para lista
# print(l2) # Lista organizada e sem valores repetidos

# # Os set não garantem ordem e não aceitam valores mutáveis
# s1 = set('Luis')
# print(s1)

# s1 = {1, 2, 3}
# print(s1)

# for numero in s1:
#     print(numero, end=' ')


# Métodos úteis:
# # add, update, clear, discard
# s1 = set()
# s1.add('Luis')
# s1.add(1)

# s1.update((1, 2, 3, 4, 'Olá, Mundo'))
# # s1.clear()
# print(s1)
# s1.discard('Olá, Mundo') # Como o set não possui indexação, para descartar tal valor é necessário indicar ele dentro do corpo da função
# s1.discard('Luis')
# print(f'Set após ter descartado "Olá, Mundo" e "Luis": {s1}')

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # União
s4 = s1 & s2 # Intersecção
s5 = s1 - s2 # Diferença
s6 = s1 ^ s2 # Diferença simétrica

print(f'Conjunto(set) s1: {s1}')
print(f'Conjunto(set) s2: {s2}')
print()
print(f'Conjunto da união de s1 e s2 (s1 | s2): {s3}')
print(f'Conjunto da intersecção de s1 e s2 (s1 & s2): {s4}')
print(f'Conjunto da diferença entre s1 e s2 (s1 - s2): {s5}')
print(f'Conjunto da diferença simétrica(que não está presente nos dois) entre s1 e s2 (s1 ^ s2): {s6}')
