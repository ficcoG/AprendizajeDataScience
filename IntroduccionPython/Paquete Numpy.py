#Paquete numpy

import numpy as np

lista = [2,4,6,8,10,12]
vector = np.array(lista) #Deben ser del mismo tipo

print("Lista original:")
print(lista)

print("\nVector convertido")
print(vector)

print("\n\nVector mas 1")
print(vector + 1)

print("\nVector por dos")
vector2 = vector * 2
print(vector2)

print("\nLista por dos") #Duplica la lista
print(lista * 2)

print("\nVector 1 mas vector 2")
print(vector + vector2)

