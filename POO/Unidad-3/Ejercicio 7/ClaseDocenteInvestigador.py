from __future__ import annotations
from ClaseDocente import Docente
from ClaseInvestigador import Investigacion

class DocenteInvestigador(Docente,Investigacion):
    __categoria:str = ""
    __importe:float = 0.0

    def __init__(self,datos:dict):
        super().__init__(datos)
        self.__categoria = str(datos['categoria'])
        self.__importe = float(datos['importe'])

    def SueldoDI(self):
        sueldoDI = self.SueloaCobrar() + self.__importe
        return sueldoDI

    def getExtra(self):
        return self.__importe

    def getCatetoria(self):
        return self.__categoria
    
    def __lt__(self,otro:DocenteInvestigador):
        return self.getNombre() < otro.getNombre()

    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil =  self.getCUIL(),
                apellido = self.getApellido(),
                nombre = self.getNombre(),
                sueldoB = self.getSueldoB(),
                antiguedad = self.getAntiguedad(),
                carrera = self.getCarrera(),
                cargo = self.getCargo(),
                catedra = self.getCatedra(),
                areaInvestigacion=  self.getArea(),
                tipoInvestigacion= self.getTipo(),
                categoria = self.__categoria,
                importe = self.__importe
            )
        )
        return d