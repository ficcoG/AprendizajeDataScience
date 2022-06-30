#Paquete numpy - error, estadistica y matriz

import numpy as np

lista1 = [2,4,6,7]
lista2 = [1,2,3]

v1 = np.array(lista1)
v2 = np.array(lista2)

#print(v1 + v2) Error porque tienen diferentes dimensiones

print("Lista 1:",lista1)
print("Lista 2:",lista2)

print("Vector 1",v1)
print("Vector 1",v1)

#Media
prom1 = np.mean(v1)
prom2 = np.mean(v2)

print("\nMedias")
print("Media de vector 1:",prom1)
print("Media de vector 2:",prom2)

v3 = v1[1:3]
print("\n\nSlice de 2 elementos: ",v3)

v4 = np.zeros(3)
v5 = np.ones(4)

print("\n\nVector de 0s: ",v4)
print("\nVector de 1s: ",v5)

dims = (3,4)

matriz = np.zeros(dims)
print("\n\nMatriz\n",matriz)
print("\nTamaño matriz: ",matriz.shape)

matriz[1,2] = 3
print("\n\nMatriz alterada\n",matriz)















