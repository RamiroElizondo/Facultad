import csv
from ClaseJugador import Jugador


class ManejadaorJugador:
    __listaJugador: list[Jugador]

    def __init__(self):
        self.__listaJugador = []
    
    def cargarJugador(self):
        with open("jugadores.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Jugador(linea[0],linea[1],linea[2],linea[3],linea[4])
                self.__listaJugador.append(objeto)
        for objetoE in self.__listaJugador:
            print(objetoE)
    def getListaJ(self):
        return self.__listaJugador
        