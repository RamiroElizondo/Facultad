from ClasePersonal import Personal
class Investigacion(Personal):
    __areaInvestigacion:str = ""
    __tipoInvestigacion:str = ""

    def __init__(self,datos:dict):
        super().__init__(datos)
        self.__areaInvestigacion = str(datos['areaInvestigacion'])
        self.__tipoInvestigacion = str(datos['tipoInvestigacion'])
    
    def getArea(self):
        return self.__areaInvestigacion
    
    def getTipo(self):
        return self.__tipoInvestigacion

    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil =  self.getCUIL(),
                apellido = self.getApellido(),
                nombre = self.getNombre(),
                sueldoB = self.getSueldoB(),
                antiguedad = self.getAntiguedad(),
                areaInvestigacion=  self.__areaInvestigacion,
                tipoInvestigacion= self.__tipoInvestigacion,
            )
        )
        return d