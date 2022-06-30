#Ingreso de datos, casting y operaciones

import math

var1 = input("Ingrese datos: ")
print("\n \n")
print(var1)

num1 = int(var1)
print(num1)
print(num1 + 10)

#Operaciones aritmeticas

print(num1 + 10)
print(num1 - 6)
print(num1 * 10)
print(num1 / 10)
print(num1 // 10) #Division entera
print(num1 % 10) #Modulo, resto de la division
print(math.sqrt(num1))
print(10/2) #La division es flotante

#Operaciones logicas: < , <= , > , >= , == , != , and , or , in

print( "\n\n Operaciones logicas")
print(num1 > 34)
print(num1 <= 34)
print(num1 == 100)
print(num1 != 100)
print(num1 >0 and num1 < 100)
print(num1 > 100 or num1 <0)
