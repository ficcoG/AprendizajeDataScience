# Tarea 1.44 Crear una tupla con los siete días de la semana
#  Recorrer los 365 días del año 2022 Para cada día del año 
#  imprimir el nombre del día de la semana

tupla = ("Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado")

for i in range(1,25):
    print(tupla[(i+5)%7]) #El 2022 empieza un sabado por eso modifique i para que empieze por ese dia
    
    