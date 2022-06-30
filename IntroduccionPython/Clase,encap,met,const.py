#Definicion de clase, con encapsulamiento, metodo y constructor

class Coche():
    
    def __init__(self,marca1): #Se ejecuta cuando se crea el objeto / Metodo constructor
        self.__marca = marca1    
    
    def verMarca(self):
        return self.__marca
    

auto1 = Coche("Ford")
auto2 = Coche("Fiat")

print("La marca del auto 1 es: ",auto1.verMarca())
print("La marca del auto 2 es: ",auto2.verMarca())

print(auto1)
print(type(auto1))
