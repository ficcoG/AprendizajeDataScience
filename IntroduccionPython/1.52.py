# 1.52 Construya un generador que vaya recorriendo la sucesión aritmética: 1, 2, 3, 4, 5 …
#  Imprima por pantalla los 10 primeros valores

def arit():
    numero = 1
    while True:
        yield numero
        numero += 1

serie = arit()
for i in range(10):
    print(next(serie),end=(" "))

