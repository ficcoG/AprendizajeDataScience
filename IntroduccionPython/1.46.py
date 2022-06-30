# Tarea 1.46 Crear una tupla t1 con las longitudes de los meses del año 2019
#  Crear una tupla t2 con los nombres de los meses del año
#  Recorrer el año mostrando por pantalla el número de día dentro del año
#  y el número del día dentro del mes.y el nombre del mes

tupla = (31,28,31,30,31,30,31,31,30,31,30,31)
tupla2= ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
         "Agosto","Septiembre","Octubre","Noviembre","Diciembre")

j=0
h=1
for i in range(1,65):
    
    if h != tupla[j]:
        dia_mes=h
        h = h + 1
        mes = tupla2[j]
    elif h == tupla[j]:
        dia_mes = h
        h = 1
        mes = tupla2[j]
        j = j + 1
    
    print("Dia del año: ",i, "Dia ",dia_mes," de ",mes)
    


