lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)

# Dois for com list comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, letra) for letra in 'Graco']
    for x in range(3)
]

print(lista)