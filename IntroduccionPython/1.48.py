# Tarea 1.48 Crear una tupla t1 con las longitudes de los meses del año 2019
#  Crear una tupla t2 con los nombres de los meses del año
#  Crear una tupla t3 con los nombres de los días de la semana
#  Crear una lista con las fechas largas que hemos mostrado por pantalla en el ejercicio 1.46 
#  (nombre del día dentro de la semana, número del día dentro del mes, nombre del mes)

dias = (31,28,31,30,31,30,31,31,30,31,30,31)
meses= ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
         "Agosto","Septiembre","Octubre","Noviembre","Diciembre")
semana = ("Viernes","Sabado","Domingo","Lunes","Martes","Miercoles","Jueves")
lista = []

j=0
h=1
for i in range(1,65):
    
    if h != dias[j]:
        dia_mes=h
        h = h + 1
        mes = meses[j]
        dia_semana = semana[i%7]
        
    elif h == dias[j]:
        dia_mes = h
        h = 1
        mes = meses[j]
        j = j + 1
        dia_semana = semana[i%7]
    fecha = dia_semana,str(dia_mes),mes
    lista.append(fecha)
    
    print(lista[i-1])
    

    
    
    


