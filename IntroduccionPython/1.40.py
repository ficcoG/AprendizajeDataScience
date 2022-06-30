# Tarea 1.40 Tomar el diccionario generado en el ejercicio 1.38 y
#  cambiar cada valor letras mayúsculas Imprimir el resultado

d = {"a":"Domingo","b":"Lunes","c":"Martes","d":"Miercoles","e":"Jueves","f":"Viernes","g":"Sabado"}

for i in d.keys():
    d[i] = d[i].upper()
    


print("Diccionario\n")
print(d)


    