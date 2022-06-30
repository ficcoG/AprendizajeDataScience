#Definicion de clase, con encapsulamiento y metodo

class Coche():
    __marca= "Toyota" #El atributo es privada para la clase, no se puede acceder de otro lado (Mediante "__")
    
    def verMarca(self): #Parametro self, puntero a si mismo
        return self.__marca
    
    

auto1 = Coche()
auto2 = Coche()


# print("La marca del auto 1 es: ",auto1.__marca) No se puede acceder

print("La marca del auto 1 es: ",auto1.verMarca()) #De esta manera se puede acceder al atributo
# print(dir(Coche)) #Para ver los metodos de la clase

