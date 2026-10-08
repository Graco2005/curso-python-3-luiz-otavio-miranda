# Escopo da classe e métodos da classe

class Animal():
    # nome = 'Leão'

    def __init__(self, nome='animal'):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento='algo'):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)



leao = Animal(nome='Leão')
print(leao.nome)

# leao.comendo('carne')

print(leao.executar('Maçã'))