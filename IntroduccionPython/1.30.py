# Tarea 1.30 Crear una lista l1 con todos los impares de 1 a 5 
# Insertar los pares en los lugares correspondientes para que la lista quede ordenada 
# Imprimir l1

lista = []

for i in range(1,6):
    if i%2 !=0:
        lista.append(i)

print("\nLista Impares")
print(lista)
        
for i in range(len(lista)):
    if i%2 ==0:
        lista.insert(i, i)

print("\nLista completa")
print(lista)

