# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:

    ano = 2026 # Atributos de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def falar_oi(cls):
        print('Oi')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('Luis', 20)
p2 = Pessoa.criar_com_50_anos('Marina')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(20)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# p1.falar_oi()
# Pessoa.falar_oi(p1)
