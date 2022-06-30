#Funciones generadoras
#Construya un generador que vaya recorriendo la serie que va sumando la sucesion aritmetica: 1, 3, 6, 10
#Imprima por pantalla los primeros valores

def arit():
    numero  = 0
    paso = 1
    while True:
        numero = numero + paso
        yield numero #yield devuelve el valor pero no borra lo demas
        paso = paso + 1

#Programa

serie = arit() #Tipo generator
print((next(serie))) #Para poder imprimir un generator
print((next(serie)))
print((next(serie)))
print((next(serie)))
print((next(serie)))




# call 1:
#     numero = 0
#     paso = 1
#     numero =1
#     -> numero = 1
    
# call 2:
#     numero = 1 -> 3
#     paso = 1 -> 2
#     -> numero = 3

# call 3:
    