import json

# pessoa = {
#     'nome': 'Luis Graco',
#     'sobrenome': 'Capistrano',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (8, 47, 100),
#     'dev': True,
#     'nada': None
# }

# with open('aula57.json', 'w') as arquivo:
#     json.dump(pessoa, arquivo, indent=2)

with open('aula57.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])