"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""

def multiplicando(multiplicador):
    def multiplicar(numero):
        return f'Multiplicador x{multiplicador} x {numero} = {multiplicador * numero}'
    return multiplicar

duplicar = multiplicando(2)
triplicar = multiplicando(3)
quadruplicar = multiplicando(4)

print(duplicar(10))
print(triplicar(3))
print(quadruplicar(100))