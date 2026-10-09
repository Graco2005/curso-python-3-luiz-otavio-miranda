# Atributos de classe
class Pessoa:
    ano_atual = 2026 # <- Atributo

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('Luis', 20)
p2 = Pessoa('Godofreldo', 89)

print(f'Nome: {p1.nome}, idade: {p1.idade}, ano atual: {p1.ano_atual}, ano de nascimento: {p1.get_ano_nascimento()}')
print(f'Nome: {p2.nome}, idade: {p2.idade}, ano atual: {p2.ano_atual}, ano de nascimento: {p2.get_ano_nascimento()}')
