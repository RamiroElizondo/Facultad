class Vehiculo:
    __cargaMax = None

    def __init__(self, cargaMax):
        self.__cargaMax = cargaMax
    
    def mostrar(self, tipo = 'Vehiculo'):
        print('Tipo: ', tipo)
        print('Carga maxima: ', self.__cargaMax)

class VehiculoConMotor(Vehiculo):
    __autonomia = None

    def __init__(self, cargaMax, autonomia):
        super().__init__(cargaMax)
        self.__autonomia = autonomia

    def mostrar(self):
        super().mostrar('Vehiculo con motor')
        print('Autonomia: ', self.__autonomia)


class VehiculoSinMotor(Vehiculo):
    __tipo = None

    def __init__(self, cargaMax, tipo):
        super().__init__(cargaMax)
        self.__tipo = tipo

    def mostrar(self):
        super().mostrar('Vehiculo sin motor')
        print('Tipo: ', self.__tipo)

    def getTipo(self):
        return self.__tipo

class Manejador:
    __lista = None

    def __init__(self):
        self.__lista = []

    def cargar(self, vehiculo):
        if(isinstance(vehiculo, VehiculoConMotor) or isinstance(vehiculo, VehiculoSinMotor)): # isinstace(vehiculo, Vehiculo)
            self.__lista.append(vehiculo)
        else:
            raise Exception('El vehiculo no es valido')

    def mostrarBicicletas(self):
        for vehiculo in self.__lista:
            if(isinstance(vehiculo, VehiculoSinMotor) and vehiculo.getTipo() == 'Bicicleta'):
                vehiculo.mostrar()

if __name__ == '__main__':
    man = Manejador()
    man.cargar(VehiculoSinMotor('50kg','Bicicleta'))
    man.mostrarBicicletas()