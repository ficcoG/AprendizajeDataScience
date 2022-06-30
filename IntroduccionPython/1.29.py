# Tarea 1.29 Crear una lista l1 con todos los días de la semana 
# Crear una lista l2 con los días hábiles de la semana Recorrer l1 e
#  indicar para cada elemento si se encuentra o no en l2

l1 = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
l2 = ["Lunes","Martes","Miercoles","Jueves","Viernes"]

for dia in l1:
    if dia in l2:
        print("El dia ", dia, " es un dia habil")
    else:
        print("El dia ",dia, " no es un dia habil")
        