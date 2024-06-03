from ClaseVehiculo import Vehiculo #Primero es de que archivo y luego que clase


class Camioneta(Vehiculo):
    __cargaMaxima:int = 0

    def __init__(self,marca,modelo,año,cargaMaxima):
        super().__init__(marca,modelo,año)
        self.__cargaMaxima = cargaMaxima

    def obtenerInformacion(self):
        return 'Marca: ' + self.getMarca() +'\tModelo: '+  self.getModelo() +'\tAño: '+ self.getAño() +'\tCarga: '+ self.__cargaMaxima

    
if __name__ == '__main__':
    objeto = Camioneta('Toyota','Turbo','2000','1000')
    print(objeto.obtenerInformacion())    
