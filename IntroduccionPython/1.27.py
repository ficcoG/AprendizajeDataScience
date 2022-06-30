# Tarea 1.27 Crear una lista con los días de la semana
#  Eliminar de la lista el sábado y el domingo
#  Mostrar el contenido de la lista con un único print

lista = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]

lista.pop(0)
lista.pop(5)

print("\nLista")
print(lista)