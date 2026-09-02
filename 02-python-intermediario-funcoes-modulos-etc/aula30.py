# Introdução às Generator Functions em Python
# generator = (n for n in range(1000))

def generator(n=0, maximum=10):
    print(f'De {n} até {maximum}')
    while True:
        yield n
        n += 1

        if n > maximum:
            return 'MÁXIMO'


gen = generator()

for n in generator(maximum=50):
    print(n)
