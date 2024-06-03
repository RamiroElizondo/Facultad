from ClaseCalefactor import Calefactor


class CalGas(Calefactor):
    __matricula:str = ""
    __calorias:int = 0

    def __init__(self,marca,modelo,matricula,calorias):
        super().__init__(modelo,marca)
        self.__matricula = matricula
        self.__calorias = calorias
    
    def CostoG(self,costoM3,cantM3):
        costo = (self.__calorias/1000)*cantM3*costoM3
        return costo
    
    def getMatricula(self):
        return self.__matricula
    
    def getCalorias(self):
        return self.__calorias