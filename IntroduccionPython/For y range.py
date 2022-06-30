#Bucle FOR y coleccion range

rango1 = range(10) #0 1 2 3 4 5 6 7 8 9
rango2 = range(50,61) #50 51 52 53 54 55 56 57 58 59 60
rango3 = range(20,41,2) #20 22 24 26 28 30 32 34 36 38 40
rango4 = range(100,79,-2)

print(rango1 ,end=(" ")) #Coleccion autocontenida para sacar los valor se debe poner "*"
print(*rango1)

print(rango2, end=(" "))
print(*rango2)

print(rango3,end=(" "))
print(*rango3)

print(rango4,end=(" "))
print(*rango4)

# for variableIterable in [coleccion]:
#     instruccion1
#     instruccion2

# [Coleccion]: str, lista, tupla, diccionario,range

print("\nFOR")
for dato in range(10):
    print(dato)

print("\nLISTA")
lis=[]

for valor in range(1,10):
    lis.append(valor)
    print(lis)
print("\n\nLista completa: ",lis)

print("\nLista 2")
lista2 = [2,3,True,"hola que tal",6+9j]

for i in lista2:
    print(i)

print("\nDiccionario")
dic1 = {1:100,2:40,3:"hola"}

for j in dic1:
    print(j,dic1[j])

print("\nRecorriendo un string")
for h in "hola que tal":
    print(h)







