# Herança simples - Relações entre classes
#
# Associação -> usa
# Agregação -> tem
# Composição -> É dono de
# Herança -> É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa():
  cpf = '1234'

  def __init__(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome

  def falar_nome_classe(self):
    print(f'Nome: {self.nome}, sobrenome: {self.sobrenome}, nome da classe: {self.__class__.__name__}')


class Cliente(Pessoa):
  ...

class Aluno(Pessoa):
  cpf = 'cpf aluno'
  ...


c1 = Cliente('Luis', 'Capistrano')
c1.falar_nome_classe()

a1 = Aluno('Marina', 'Castro')
a1.falar_nome_classe()

# help(Aluno)
