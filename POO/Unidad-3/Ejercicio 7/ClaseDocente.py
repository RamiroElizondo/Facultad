from ClasePersonal import Personal

class Docente(Personal):
    __carrera:str = ""
    __cargo:str = ""
    __catedra:str = ""

    def __init__(self,datos:dict):
        super().__init__(datos)
        self.__carrera = str(datos['carrera'])
        self.__cargo = str(datos['cargo'])
        self.__catedra = str(datos['catedra'])

    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra

    def sueldoDocente(self):
        sueldoD = self.getSueldoB()
        porcentaje:float = 0.0
        if self.__cargo == 'Simple':
            porcentaje = 0.10
        elif self.__cargo == 'Semiexclusivo':
            porcentaje = 0.20
        elif self.__cargo == 'Exclusivo':
            porcentaje = 0.50
        return self.SueloaCobrar() + (sueldoD*porcentaje)

    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil =  self.getCUIL(),
                apellido = self.getApellido(),
                nombre = self.getNombre(),
                sueldoB = self.getSueldoB(),
                antiguedad = self.getAntiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra
            )
        )
        return d
    