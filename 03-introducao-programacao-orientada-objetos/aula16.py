# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
  def __init__(self, nome):
    self.nome = nome
    self.enderecos = []

  def inserir_enderecos(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero))

  def inserir_enderecos_externos(self, endereco):
      self.enderecos.append(endereco)

  def listar_enderecos(self):
    for endereco in self.enderecos:
      print(f'Rua: {endereco.rua}, Número: {endereco.numero}')

  def __del__(self):
      print('APAGANDO', self.nome)

class Endereco:
  def __init__(self, rua, numero):
    self.rua = rua
    self.numero = numero

  def __del__(self):
    print('APAGANDO', self.rua, self.numero)


cliente = Cliente('Marina')
cliente.inserir_enderecos('Rua parangada', 14)
cliente.inserir_enderecos('Washington Soares', 3030)
endereco_externo = Endereco('Luciano Carneiro')
cliente.inserir_enderecos_externos(endereco_externo)

cliente.listar_enderecos()

del cliente

print(endereco_externo.rua, endereco_externo.numero)
