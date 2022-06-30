# Tarea 1.23 Ingresar por teclado dos enteros y almacenarlos en a y b. 
# Crear una función de dos parámetros que devuelve la suma de esos parámetros
#  Usar la función creada para calcular la suma de a y b. 
#  Mostrar por pantalla el resultado de la suma

a = int(input("Ingrese un numero "))
b = int(input("Ingrese un numero "))

def suma(a,b):
    c = a + b
    return c

print("La suma es ",suma(a,b))

