# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade=None):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'Luis', 'idade': 20}

p1 = Pessoa(**dados) # Desempacotando os dados com **
# p1.nome = 'Marina'
# del p1.nome
# print(p1.nome)

# Vars e dict possuem a mesma função de agir como 'toString' da classe, mostrando os seus atributos.
print(p1.__dict__)
print(vars(p1))

p1.__dict__['outra'] = 'coisa' # Adicionando um atributo diretamente no dicionário
print(p1.__dict__)
print(vars(p1))

del p1.__dict__['nome'] # Apagando o atributo/chave 'nome'
print(p1.__dict__)
print(vars(p1))
