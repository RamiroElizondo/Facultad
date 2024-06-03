from ClaseVehiculo import Vehiculo
class Concesionario:
    __nombre:str = ""
    __vehiculos: list[Vehiculo]

    def __init__(self,nombre):
        self.__nombre = nombre
        self.__vehiculos = []
    
    def agregarVehiculo(self,vehiculo):
        self.__vehiculos.append(vehiculo)
    
    def listarVehiculo(self):
        return self.__vehiculos
    
