from ast import Eq
import csv
import numpy
from ClaseEquipo import Equipo


class ManejadorEquipos:
    __arreglo: numpy.ndarray

    def __init__(self):
        self.__arreglo = numpy.empty(0, dtype=Equipo)

    def cargarEquipo(self):
        with open('equipos.csv','r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Equipo(linea[0],linea[1])
                self.__arreglo = numpy.append(self.__arreglo,objeto) # type: ignore

        """for objetoE in self.__arreglo:
            print(objetoE)"""
    
    def getEquipos(self):
        return self.__arreglo