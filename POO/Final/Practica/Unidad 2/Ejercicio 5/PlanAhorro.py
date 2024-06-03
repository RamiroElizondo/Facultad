class PlanAhorro:
    __codPlan:int = 0
    __modelo = ""
    __version = ""
    __valor:int = 0
    __cantidadCuotasP:int = 0
    __cantidadCuotasPagar:int = 0

    def __init__(self,cod,modelo,version,valor):
        self.__codPlan = cod
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    @classmethod
    def setcantidadCuotasP(cls,valor):
        cls.__cantidadCuotasP = valor
    
    @classmethod
    def setcantidadCuotasPagar(cls,valor):
        cls.__cantidadCuotasPagar = valor

    @classmethod
    def getcantCuotasP(cls):
        return cls.__cantCuotasP

    @classmethod
    def getcantCuotasLicitar(cls):
        return cls.__cantCuotasLicitar
    
    def getcodPlan(self):
        return self.__codPlan
    
    def getModelo(self):
        return self.__modelo
    
    def getVersion(self):
        return self.__version
    
    def getValor(self):
        return self.__valor

    def setValor(self,valor):
        self.__valor = valor