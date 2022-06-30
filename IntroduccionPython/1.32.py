# Tarea 1.32 Crear una tupla t1 con todos los días de la semana
#  Mostrar por pantalla el número de elemento correspondiente al miércoles

tupla = ("Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado")

for i in tupla:
    if i == "Miercoles":
        print(tupla.index(i))
        
