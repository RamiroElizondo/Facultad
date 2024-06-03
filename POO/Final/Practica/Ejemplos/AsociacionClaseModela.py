class Equipo:
    __nombreE: str
    __localidad: str
    __contrato = []

    def __init__(self,nombre,localidad):
        self.__nombre = nombre
        self.__localidad = localidad
    
    def agregarContrato(self,contrato):
        self.__contrato.append(contrato)

class Jugador:
    __nombre:str
    __edad:int
    __contrato = []

    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = nombre
    
    def agregarContrato(self,contrato):
        self.__contrato.append(contrato)

    def getLista(self):
        return self.__contrato

class Contrato:
    __inicio: str 
    __fin: str 
    __jugador= None
    __equipo = None

    def __init__(self,inicio,fin,jugador,equipo):
        self.__inicio = inicio
        self.__fin = fin
        self.__jugador = jugador
        self.__equipo = equipo
        jugador.agregarContrato(self)
        equipo.agregarContrato(self)
    
    def __str__(self):
        return 'Inicio: ' + self.__inicio + ' ' + 'Fin: ' + self.__fin + ' '+'Jugador: '+ str(self.__jugador)+' '+'Equipo: '+str(self.__equipo)
    
if __name__ == '__main__':
    jugador = Jugador('Messi', 35)
    equipo = Equipo('Club Barcelona','Barcelona')
    contrato = Contrato('24/02/2023','30/10/2023',jugador,equipo)
    contrato2 = Contrato('04/11/2023','14/06/2024',jugador,equipo)
    print(contrato)
    print(jugador.getLista())

    

