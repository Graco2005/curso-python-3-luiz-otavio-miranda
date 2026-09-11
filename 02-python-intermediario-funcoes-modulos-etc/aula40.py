# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
from dados import produtos

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['nome'],
    reverse=True
)

# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['preco']
)

print('Lista normal:', *produtos, sep='\n')
print()
print('Lista de novos_produtos com preço aumentado em 10%:', *novos_produtos, sep='\n')
print()
print('Lista de produtos ordenados por nome:', *produtos_ordenados_por_nome, sep='\n')
print()
print('Lista de produtos ordenado por preço:', *produtos_ordenados_por_preco, sep='\n')