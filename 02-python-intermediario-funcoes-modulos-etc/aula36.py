# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys

import aula36_m

aula36_m.saudacao('Graco')

print('Este módulo se chama,', __name__)
# print(*sys.path, sep='\n')

from aula36_m import soma

print('Soma entre 1 e 2 utilizando a função "soma" de aula36_m:', soma(1, 2))