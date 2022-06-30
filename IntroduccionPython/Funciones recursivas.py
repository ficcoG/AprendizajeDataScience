#Funciones recursivas

#Factorial(n): 1x2x3....xn donde n es un numero entero mayor o igual a 0
#Factorial(5): 1x2x3x4x5 = 120



def Facto(num1):
    if num1 == 0:
        return 1
    elif num1 == 1:
        return 1
    else:
        temp = num1 * Facto(num1-1)
        return temp
    
#Programa

numero = 5
res = Facto(numero)

print("El factorial de 5 es:",res)
