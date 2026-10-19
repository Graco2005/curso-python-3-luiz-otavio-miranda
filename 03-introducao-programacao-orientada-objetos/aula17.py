# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
  def __init__(self, nome):
    self.nome = nome
    self._motor = None
    self._fabricante = None

  @property
  def motor(self):
    return self._motor

  @motor.setter
  def motor(self, valor):
    self._motor = valor

  @property
  def fabricante(self):
    return self._fabricante

  @fabricante.setter
  def fabricante(self, valor):
    self._fabricante = valor


class Motor:
  def __init__(self, nome):
    self.nome = nome

class Fabricante:
  def __init__(self, nome):
    self.nome = nome


fusca = Carro('Fusca')

volkswagem = Fabricante('Volkswagem')
fusca.fabricante = volkswagem

boxer = Motor('Boxer')
fusca.motor = boxer

print(f'Nome: {fusca.nome}')
print(f'Fabricante: {fusca.fabricante.nome}')
print(f'Motor: {fusca.motor.nome}')


palio = Carro('Palio')

fiat = Fabricante('Fiat')
palio.fabricante = fiat

torque = Motor('Torque')
palio.motor = torque

print()
print(f'Nome: {palio.nome}')
print(f'Fabricante: {palio.fabricante.nome}')
print(f'Motor: {palio.motor.nome}')

hb20 = Carro('Hb20')

hyundai = Fabricante('Hyundai')
hb20.fabricante = hyundai

kappa = Motor('Kappa')
hb20.motor = kappa

print()
print(f'Nome: {hb20.nome}')
print(f'Fabricante: {hb20.fabricante.nome}')
print(f'Motor: {hb20.motor.nome}')
