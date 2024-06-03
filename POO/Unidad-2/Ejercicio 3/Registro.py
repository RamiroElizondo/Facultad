class Registro:
    __temperatura = ""
    __humedad = ""
    __presion = ""

    def __init__(self, tempertaura:float, humedad:int, presion:int):
        self.__temperatura = tempertaura
        self.__humedad = humedad
        self.__presion = presion

    def muestra(self):
        return f'{self.__temperatura} {self.__humedad} {self.__presion}'

    def getTemperatura(self):
        return self.__temperatura

    def getHumedad(self):
        return self.__humedad

    def getPresion(self):
        return self.__presion
