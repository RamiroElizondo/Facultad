from ClaseCalefactor import Calefactor


class CalElectrico(Calefactor):
    __potencia:int = 0

    def __init__(self,marca,modelo,potencia):
        super().__init__(marca,modelo)
        self.__potencia = potencia
    
    def CostoE(self,costoM3,cantM3):
        costo = (self.__potencia/1000)*cantM3*costoM3
        return costo
    
    def getPotencia(self):
        return self.__potencia