# Tarea 1.21 Pidan el ingreso de dos datos a por teclado.
#  Convierta los datos a flotantes Muestre por pantalla los datos
#  ordenados de menor a mayor

a = float(input("Ingrese un numero "))
b = float(input("Ingrese un numero "))

if a>b:
    print(b,a)
elif b>a:
    print(a,b)
else:
    print("Los numeros son iguales ")
    