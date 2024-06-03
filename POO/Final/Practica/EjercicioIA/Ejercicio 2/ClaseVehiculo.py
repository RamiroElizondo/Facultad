class Vehiculo:
    __marca:str = ""
    __modelo:str = ""
    __año:str = ""

    def __init__(self,marca,modelo,año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    
    def obtenerInformacion(self):
        return self.__marca + self.__modelo + self.__año

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    
    def getAño(self):
        return self.__año