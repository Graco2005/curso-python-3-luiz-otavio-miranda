# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Luis' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luis', 'Graco')
# p1.nome = 'Luis Graco'
# p1.sobrenome = 'Capistrano'

p2 = Pessoa('Marina', 'Nunes de Castro')
# p2.nome = 'Marina'
# p2.sobrenome = 'Nunes de Castro'

print(f'Nome: {p1.nome}')
print(f'Sobrenome: {p1.sobrenome}')

print(f'Nome: {p2.nome}')
print(f'Sobrenome: {p2.sobrenome}')
