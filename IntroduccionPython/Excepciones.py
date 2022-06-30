#Excepciones

num1 = 4
num2 = "w"


try:
    res = num1/num2
    print("El cociente entre {} y {} es: {}".format(num1,num2,res))
# except ZeroDivisionError:
#     print("No se puede dividir por cero")
# except TypeError:
#     print("No se puede dividir por un string")
except Exception as dato:
    print("Error: {}".format(type(dato))) #De esta forma te guarda el error en una variable para saber cual es
    




