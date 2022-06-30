# Tarea 1.22 Ingresar por teclado una edad. Devolver por pantalla un mensaje
#  proporcionado a la edad: Menor a 15: edad de crecer De 15 a 40: edad del amor
# De 40 a 65: edad de los amigos De 65 en adelante: edad de los médicos

edad = int(input("Ingrese la edad "))

if edad < 15:
    print("Edad de crecer ")
elif edad >=15 and edad <40:
    print("Edad del amor ")
elif edad >=40 and edad < 65:
    print("Edad de los amigos ")
else:
    print("Edad de los medicos ")

