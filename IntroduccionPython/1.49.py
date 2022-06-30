# Tarea 1.49 Pedir la introducción desde el teclado de una fecha en el formato largo.
#  Usar la lista generada en el ejercicio 1.48 para encontrar el número de día dentro del año.

dias = (31,28,31,30,31,30,31,31,30,31,30,31)
meses= ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio",
         "Agosto","Septiembre","Octubre","Noviembre","Diciembre")
semana = ("Viernes","Sabado","Domingo","Lunes","Martes","Miercoles","Jueves")
lista = []

buscar = input("Ingrese la fecha a buscar ")


j=0
h=1
flag = False
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
        
    fecha = dia_semana + " " + str(dia_mes) + " de " + mes
    lista.append(fecha)
    
    
    if buscar == lista[i-1]:
        print("Es el dia ",i,"dentro del año ")
        flag = True

if flag == False:
    print("La fecha no existe o fue mal ingresada ")