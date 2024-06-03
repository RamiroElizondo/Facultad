from ClasePersonal import Personal


class PersonalApoyo(Personal):
    __categoria:int = 0
    __porcentajeycargo:list=[0,0.0]

    def __init__(self,datos:dict):
        super().__init__(datos)
        self.__categoria = int(datos['categoria'])

    
    def sueldoPersonalApoyo(self):
        valor:float = 0.0
        sueldoPA = self.getSueldoB()
        porcentaje: list[float] = [0.10,0.20,0.30]
        if self.__porcentajeycargo[1] != 0.0:
            if self.__porcentajeycargo[0] >= 1 and self.__porcentajeycargo[0] <= 10:
                porcentaje[0] = self.__porcentajeycargo[1]
            elif self.__porcentajeycargo[0] >= 11 and self.__porcentajeycargo[0] <= 20:
                porcentaje[1] = self.__porcentajeycargo[1]
            elif self.__porcentajeycargo[0] >= 21 and self.__porcentajeycargo[0] <= 22:
                porcentaje[2] = self.__porcentajeycargo[1]
        if self.__categoria >= 1 and self.__categoria <= 10:
           valor = sueldoPA * porcentaje[0]
        elif self.__categoria <= 11 and self.__categoria >= 20:
            valor = sueldoPA * porcentaje[1]
        elif self.__categoria >= 21 and self.__categoria <= 22:
            valor = sueldoPA * porcentaje[2]
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
                categoria = self.__categoria
            )
        )
        return d