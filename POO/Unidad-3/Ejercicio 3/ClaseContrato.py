from datetime import datetime
from ClaseJugador import Jugador
from ClaseEquipo import Equipo


class Contrato:
    __fechaI: datetime
    __fechaF: datetime
    __pagoM: float
    __jugador: Jugador
    __equipo: Equipo

    def __init__(self, fI, fF, pago,jugador: Jugador,equipo: Equipo):
        self.__fechaI = datetime.strptime(fI,'%d/%m/%Y')
        self.__fechaF = datetime.strptime(fF,'%d/%m/%Y')
        self.__pagoM = float(pago)
        self.__jugador = jugador
        self.__equipo = equipo
    
    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo
    
    def getPago(self):
        return self.__pagoM
    
    def getFechaInicio(self):
        return self.__fechaI
    
    def getFechaFin(self):
        return self.__fechaF