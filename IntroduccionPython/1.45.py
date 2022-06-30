# Tarea 1.45 Crear una tupla con las longitudes de los meses del año 2022
# Recorrer el año mostrando por pantalla el número de día dentro del año
#  y el número del día dentro del mes.

tupla = (31,28,31,30,31,30,31,31,30,31,30,31)
j=0
h=1
for i in range(1,65):
    
    if h != tupla[j]:
        dia_mes=h
        h = h + 1
    elif h == tupla[j]:
        j = j + 1
        dia_mes = h
        h = 1
    
    print("Dia del año: ",i, "Dia del mes ",dia_mes)
    


