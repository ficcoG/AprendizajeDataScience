#WHILE

semana = ("Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado")

ptr = 5
dia = 1

while dia <= 30:
    print("Dia ",dia, ": ",semana[ptr%7])
    ptr = ptr + 1
    dia = dia + 1
    # if ptr > 6:
    #     ptr = 0
        
