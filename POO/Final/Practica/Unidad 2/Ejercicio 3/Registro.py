class Registro:
    __temperatura = ""
    __humedad = ""
    __presionA = ""

    def __init__(self,temperatura,humedad,presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presionA = presion

    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad

    def getPresion(self):
        return self.__presionA
    
