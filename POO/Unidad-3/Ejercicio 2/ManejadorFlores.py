import csv
import numpy
from ClaseFlores import Flores


class ManejadorFlores:
    __arreglo: Flores

    def cargaFlores(self):
        lista: list[Flores] = []
        with open("Ejercicio 2\\flores.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Flores(linea[0],linea[1],linea[2],linea[3])
                lista.append(objeto)
            self.__arreglo = numpy.array(lista,dtype=Flores)
        """for objeto in self.__arreglo:
            print(objeto)"""
        return self.__arreglo