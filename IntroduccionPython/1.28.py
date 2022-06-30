# Tarea 1.28 Crear una lista con los días hábiles de la semana
#  y otra lista con el sábado y el domingo
#  Extender la primera lista con la segunda 
#  Mostrar el contenido de la lista con un único print

lista = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
lista2= ["Sabado","Domingo"]

sabado = lista2.pop(0)
domingo = lista2.pop(0)

lista.append(sabado)
lista.append(domingo)

print("\nLista")
print(lista)

