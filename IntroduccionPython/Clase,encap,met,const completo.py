#Definicion de clase, con encapsulamiento, metodo y constructor completo

class Coche():
    def __init__(self,marca1):
        self.__marca = marca1
        self.__motor = "Apagado"
        self.__luces = "Apagadas"
        
        
    def verMarca(self):
        return self.__marca
    
    def verMotor(self):
        return self.__motor
    
    def verLuces(self):
        return self.__luces
    
    def encenderMotor(self):
        self.__motor = "Encendido"
    
    def apagarMotor(self):
        self.__motor = "Apagado"
        self.__luces == "Apagadas" 
        
        
    def encenderLuces(self):
        if self.__motor == "Encendido":
            self.__luces = "Encendidas"
        else:
            print("No se pueden prender las luces con el motor apagado")
    def apagarLuces(self):
        self.__luces = "Apagadas"



auto1 = Coche("Ford")
auto2 = Coche("Fiat")

print("Datos auto 1")
print("Marca: ",auto1.verMarca())
print("Motor: ",auto1.verMotor())
print("Luces: ",auto1.verLuces())

print("\nDatos auto 2")
print("Marca: ",auto2.verMarca())
print("Motor: ",auto2.verMotor())
print("Luces: ",auto2.verLuces())

print("\n\nCAMBIOS DE ESTADO")

auto1.encenderMotor()
auto1.encenderLuces()
auto2.encenderMotor()

print("\nDatos auto 1")
print("Marca: ",auto1.verMarca())
print("Motor: ",auto1.verMotor())
print("Luces: ",auto1.verLuces())

print("\nDatos auto 2")
print("Marca: ",auto2.verMarca())
print("Motor: ",auto2.verMotor())
print("Luces: ",auto2.verLuces())

auto1.apagarMotor()
auto2.apagarMotor()
auto2.encenderLuces()

print("\n\nCAMBIOS DE ESTADO")

print("\nDatos auto 1")
print("Marca: ",auto1.verMarca())
print("Motor: ",auto1.verMotor())
print("Luces: ",auto1.verLuces())

print("\nDatos auto 2")
print("Marca: ",auto2.verMarca())
print("Motor: ",auto2.verMotor())
print("Luces: ",auto2.verLuces())














