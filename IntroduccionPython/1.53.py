# Tarea 1.53 Construya un generador que vaya recorriendo la serie que va sumando
#  la sucesión aritmética: 1, 2, 3, 6, 10, 15, 21 … Imprima por pantalla los 10 primeros valores


def arit():
    
    numero = 0
    paso = 1
    
    while True:
        numero += paso
        yield numero
        paso += 1
    
serie = arit()

for i in range(10):
    print(next(serie))
        
    
