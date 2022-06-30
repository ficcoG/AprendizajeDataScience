#Colecciones de datos:
#Tuplas -> NO SE PUEDEN CAMBIAR -> SON MUCHO MAS RAPIDAS

tupla1 = (1,2,3,"hola",True,6.8)


print(dir(tupla1))

lista1 = list(tupla1)
lista1[4] = False

tupla1 = tuple(lista1)
print((tupla1))
