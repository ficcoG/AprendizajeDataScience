# Tarea 1.54 Construya un generador que vaya recorriendo la serie geométrica: 1, 2, 4, 8, 16, 32, 64
#  … Imprima por pantalla los 10 primeros valores

def arit():
    numero = 1
    while True:
        yield numero
        numero += numero

serie = arit()

for i in range(10):
    print(next(serie),end=(" "))
    
    