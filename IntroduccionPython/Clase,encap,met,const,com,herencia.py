#Definicion de clase, con encapsulamiento, metodo y constructor completo con herencia
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

class Camioneta(Coche):
    def __init__(self,marca1,modelo1):
        Coche.__init__(self,marca1)
        self.__modelo = modelo1
        self.__carga = 0
    
    def verModelo(self):
        return self.__modelo
    
    def verCarga(self):
        return self.__carga
    
    def modCarga(self):
        carga1 = int(input("\nIngrese la carga "))
        if carga1 <= 1000:
            self.__carga = carga1
        else:
            print("No se puede cargar tanto")
        

auto1 = Coche("Fiat")
camioneta1 = Camioneta("Ford","F100")


print("Datos auto 1")
print("Marca: ",auto1.verMarca())
print("Motor: ",auto1.verMotor())
print("Luces: ",auto1.verLuces())

print("\nDatos auto 2")
print("Marca: ",camioneta1.verMarca())
print("Motor: ",camioneta1.verMotor())
print("Luces: ",camioneta1.verLuces())
print("Modelo: ",camioneta1.verModelo())
print("Carga: ",camioneta1.verCarga())

auto1.encenderMotor()
auto1.encenderLuces()
camioneta1.encenderMotor()
camioneta1.modCarga()

print("\n\nCAMBIOS DE ESTADO")

print("Datos auto 1")
print("Marca: ",auto1.verMarca())
print("Motor: ",auto1.verMotor())
print("Luces: ",auto1.verLuces())

print("\nDatos auto 2")
print("Marca: ",camioneta1.verMarca())
print("Motor: ",camioneta1.verMotor())
print("Luces: ",camioneta1.verLuces())
print("Modelo: ",camioneta1.verModelo())
print("Carga: ",camioneta1.verCarga())












