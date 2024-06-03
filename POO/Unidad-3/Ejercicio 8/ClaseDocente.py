from ClasePersonal import Personal

class Docente(Personal):
    __carrera:str = ""
    __cargo:str = ""
    __catedra:str = ""
    __porcentajeycargo:list=["",0.0]

    def __init__(self,datos:dict):
        super().__init__(datos)
        self.__carrera = str(datos['carrera'])
        self.__cargo = str(datos['cargo'])
        self.__catedra = str(datos['catedra'])

    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def setPorcentajeCargo(self,porcargo):
        self.__porcentajeycargo = porcargo

    def getCatedra(self):
        return self.__catedra

    def sueldoDocente(self):
        valor:float = 0.0
        sueldoD = self.getSueldoB()
        porcentaje: list[float] = [0.10,0.20,0.50]
        if self.__porcentajeycargo[1] != 0.0:
            if self.__porcentajeycargo[0] == 'Simple':
                porcentaje[0] = self.__porcentajeycargo[1]
            elif self.__porcentajeycargo[0] == 'Semiexclusivo':
                porcentaje[1] = self.__porcentajeycargo[1]
            elif self.__porcentajeycargo[0] == 'Exclusivo':
                porcentaje[2] = self.__porcentajeycargo[1]
        
        if self.__cargo == 'Simple':
            valor = sueldoD * porcentaje[0]
        elif self.__cargo == 'Semiexclusivo':
            valor = sueldoD * porcentaje[1]
        elif self.__cargo == 'Exclusivo':
            valor = sueldoD * porcentaje[2]
        return self.SueloaCobrar() + valor

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
    