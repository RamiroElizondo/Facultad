class Personal:
    __cuil:str = ""
    __apellido:str = ""
    __nombre:str = ""
    __sueldoB:float = 0.0
    __antiguedad:int = 0

    def __init__(self,datos:dict):
        self.__cuil = str(datos['cuil'])
        self.__apellido = str(datos['apellido'])
        self.__nombre = str(datos['nombre'])
        self.__sueldoB = float(datos['sueldoB'])
        self.__antiguedad = int(datos['antiguedad'])

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def setSueldoB(self,nuevo):
        self.__sueldoB = nuevo
    def getSueldoB(self):
        return self.__sueldoB

    def SueloaCobrar(self):
        self.__sueldoB = self.__sueldoB + (self.__sueldoB * 0.05)
        return self.__sueldoB
    
    def getCUIL(self):
        return self.__cuil
    
    def getAntiguedad(self):
        return self.__antiguedad