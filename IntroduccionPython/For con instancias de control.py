#FOR con instancias de control

lis=[]

for valor in range(1,10):
    if valor == 5:
        print("Valor encontrado")
        #pass -> No hace nada, placebo
        #continue -> Pasa a la siguiente iteracion, se olvida del resto del codigo que sigue
        #break -> Frena el bucle
    lis.append(valor)
    print(lis)
print("\n\nLista completa: ",lis)

