# Exemplo de uso de sets

letras = set() # ou {}

while True:
    letra = input('Digite letras: ').lower()
    letra_primeira = letra[0]


    if not letra_primeira.isdigit():
        letras.add(letra_primeira)
        print(letras)
    else:
        print('Digite letras, não numeros!')

    if 'l' in letras:
        print('Você achou a letra secreta. BREAK!')
        break