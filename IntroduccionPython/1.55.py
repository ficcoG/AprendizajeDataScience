# 1.55 Construya un generador que vaya recorriendo la suma de la serie geométrica:
#     1, 3, 7, 15, 31, 63, 127 Imprima por pantalla los 10 primeros valores

def arit():
    numero = 1
    paso = 2
    while True:
        yield numero
        numero += paso
        paso *= 2
        

serie = arit()

for i in range(10):
    print(next(serie),end=(" "))
    
