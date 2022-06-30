# Tarea 1.39 Crear una tupla con la siete primeras letras del alfabeto 
# Recorrer la tupla y usarla como clave para imprimir los valores del 
# diccionario construido en la tarea 1.38

d = {"a":"Domingo","b":"Lunes","c":"Martes","d":"Miercoles","e":"Jueves","f":"Viernes","g":"Sabado"}
tupla = ("a","b","c","d","f","g")

print("Diccionario\n")
for i in tupla:
    print(d[i])

