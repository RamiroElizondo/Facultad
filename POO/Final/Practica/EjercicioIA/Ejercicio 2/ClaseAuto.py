from ClaseVehiculo import Vehiculo


class Auto(Vehiculo):
    __puertas:int = 0

    def __init__(self,marca,modelo,año,puertas):
        super().__init__(marca,modelo,año)
        self.__puertas = puertas
    
    def obtenerInformacion(self):
        return self.getMarca() + self.getModelo() + self.getAño() + self.__puertas
    
