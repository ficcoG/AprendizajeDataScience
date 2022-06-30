
#Macro -> Secuencia fija 

# if condicion1:
#     asdasd
#     asdasd
# elif condicion2:
#     asdasda
#     asdasda
#     asdasd
# else:
#     asdasda
#     asdadasd

# switch case -> NO ESTA IMPLEMENTADO

#Ejercicio -> Pedir un numero, y ver si es cero, par o impar

a = int(input("Ingrese un numero "))

if a==0:
    print("El numero es 0 ")
elif a %2 ==0:
    print("El numero es par")
else:
    print("El numero es impar")

#Es conveniente dejar un else para los casos en los que no se conoce
# explicitamente las condiciones