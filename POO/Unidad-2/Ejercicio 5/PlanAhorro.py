class PlanAhorro:
    __codP: int = 0
    __modelo: str = ""
    __version: str = ""
    __valorVehiculo: int = 0
    __cantCuotasP: int = 0
    __cantCuotasLicitar: int = 0

    def __init__(self, codP: int, modelo: str, version: str, valorVehiculo: int):
        self.__codP = codP
        self.__modelo = modelo
        self.__version = version
        self.__valorVehiculo = valorVehiculo

    def getcod(self):
        return self.__codP

    def muestra(self):
        return print('Codigo Plan: {} Modelo: {} Version: {}'.format(self.__codP,self.__modelo,self.__version))

    def setvalorVehiculo(self, valorNuevo:int):
        self.__valorVehiculo = valorNuevo
        print('Se cambio el valor'.center(30,'-'))
    
    def getvalorVehiculo(self):
        return self.__valorVehiculo

    @classmethod
    def setcantCuotasP(cls, valor:int):
        cls.__cantCuotasP = valor

    @classmethod
    def setcantCuotasLicitar(cls, valor:int):
        cls.__cantCuotasLicitar = valor

    @classmethod
    def getcantCuotasP(cls):
        return cls.__cantCuotasP

    @classmethod
    def getcantCuotasLicitar(cls):
        return cls.__cantCuotasLicitar
        
    def __str__(self):
        return f'{self.__codP} {self.__modelo} {self.__version} {self.__valorVehiculo}'
    
    @classmethod
    def mostrar(cls):
        print('Cantidad cuotas: '+ str(cls.getcantCuotasP()),end=' ')
        print('Cantidad cuotas a licitar: '+ str(cls.getcantCuotasLicitar()))