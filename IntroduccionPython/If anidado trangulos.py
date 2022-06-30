#IF anidado sobre triangulos

lado1 = int(input("Introduzca lado 1: "))
lado2 = int(input("Introduzca lado 2: "))
lado3 = int(input("Introduzca lado 3: "))

lados = [lado1,lado2,lado3]
lados.sort()
print("Lados ordenados: ",lados)

if lados[0] + lados[2] < lados[2]:
    print("No corresponde a los lados de un triangulo ")
elif lados[0] + lados[1] == lados[2]:
    print("Es un triangulo cerrado ")
else:
    if lados[0] == lados[1] and lados[1] == lados[2]:
        print("Es un triangulo equilatero")
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print("Es un triangulo isosceles ")
    else:
        print("Es un triangulo escaleno ")
        
    
