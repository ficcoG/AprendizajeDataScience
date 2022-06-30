#Programa que divide dos numeros ingresados por teclado por un usuario no muy inteligente


while True:
    try:
        a = int(input("Ingrese dividendo: "))
        break
    except ValueError:
        print("El valor ingresado no es valido")
    
while True:
    try:
        b = int(input("Ingrese divisor "))
        break
    except ValueError:
        print("El valor ingresado no es valido")
    
    

try:
    resultado = a/b
    print("La division entre {} y {} es: {}".format(a,b,resultado))
except ZeroDivisionError:
    print("No se puede dividir por cero")
    