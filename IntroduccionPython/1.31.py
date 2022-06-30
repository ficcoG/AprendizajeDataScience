# Tarea 1.31 Crear una lista l1 con todos los días de la semana 
# Imprimir la longitud de l1 
# Extender l1 con si misma Imprimir la longitud de l1

lista = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]

print("Longitud de la lista")
print(len(lista))

# lista.append(lista)
# print("\nLongitud de la lista")
# print(len(lista))
# print(lista)

for i in range(7):
    lista.append(lista[i])
    
print("\nLista extendida por si misma")
print(lista)
print("\nLongitud de la lista")
print(len(lista))
