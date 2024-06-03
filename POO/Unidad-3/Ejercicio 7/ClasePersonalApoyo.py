from ClasePersonal import Personal


class PersonalApoyo(Personal):
    __categoria:int = 0

    def __init__(self,datos:dict):
        super().__init__(datos)
        self.__categoria = int(datos['categoria'])

    def sueldoPersonalApoyo(self):
        suedoPA = self.getSueldoB()
        porcentaje:float = 0.0
        if self.__categoria >= 1 and self.__categoria <= 10:
            porcentaje = 0.10
        elif self.__categoria <= 11 and self.__categoria >= 20:
            porcentaje = 0.20
        elif self.__categoria >= 21 and self.__categoria <= 22:
            porcentaje = 0.30
        return self.SueloaCobrar() + (suedoPA * porcentaje)
    
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