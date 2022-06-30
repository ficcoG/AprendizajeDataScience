#Colecciones de datos: 
#Lista -> NO ES UN VECTOR

lista1 = [1,2,3,4, "hola", True , 3.5]

print(lista1)

print(lista1 * 2)
print("Largo: " ,len(lista1))
print(lista1[6])

#Metodos
lista1.append("END")
lista1.insert(1,100)
print(lista1)
lista1.pop(1)
print(lista1)

lista2 = [10,24,15,2]
print(lista2)
lista2.sort() #Ordena
print(lista2)
lista2.sort(reverse=True)

lista3 = []
lista3.append(lista2)
print(lista3)
lista3.append(lista2)
print(lista3) #Parecida pero NO ES UNA MATRIZ
print(lista3[0][2])
lista3.clear()
print(lista3)

print(dir(lista1)) #Los metodos que soporta la lista

