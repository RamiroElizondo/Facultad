"""
Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo.
"""
import numpy
import csv
from ClaseCalefactor import Calefactor
from ClaseCalElectrico import CalElectrico
from ClaseCalGas import CalGas


class ManejadorCalefactor:
    __arreglo: numpy.ndarray

    def __init__(self):
        self.__arreglo = numpy.empty(0, dtype=Calefactor)
    
    def Cargar(self,archivo1,archivo2,tamaño):
        self.__arreglo = numpy.empty(tamaño, dtype=Calefactor)
        readerG = csv.reader(archivo1, delimiter=';')
        readerE = csv.reader(archivo2, delimiter=';')
        next(readerG,None)
        next(readerE,None)
        i:int = 0
        for gas in readerG:
            self.__arreglo[i] = CalGas(gas[0],gas[1],gas[2],gas[3])
            i += 1
        for electrico in readerE:
            self.__arreglo[i] = CalElectrico(electrico[0],electrico[1],int(electrico[2]))
            i += 1

        """for objeto in self.__arreglo:
            print(objeto)"""
    
    def MenorConsumoGas(self):
        costoM3 = float(input("Ingrese el costo por m3: "))
        cantM3 = int(input("Ingrese la cantidad de m3 que se estima consumir: "))
        menor = self.__arreglo[0]
        i:int = 0
        indice:int = 0
        for objeto in self.__arreglo:
            if isinstance(objeto,CalGas):
                if objeto.CostoG(costoM3,cantM3) < menor.CostoG(costoM3,cantM3):
                    menor = objeto
                    indice = i
            i += 1
        print('Marca: {} Modelo: {}'.format(menor.getMarca(),menor.getModelo()))
        return indice

    def MenorConsumoElectrico(self):
        costoM3 = float(input("Ingrese el costo por m3: "))
        cantM3 = int(input("Ingrese la cantidad de m3 que se estima consumir: "))
        menor = self.__arreglo[0]
        i:int = 0
        indice:int = 0
        for objeto in self.__arreglo:
            if isinstance(objeto,CalElectrico):
                if objeto.CostoE(costoM3,cantM3) < menor.CostoE(costoM3,cantM3):
                    menor = objeto
                    indice = i
            i += 1
        print('Marca: {} Modelo: {}'.format(menor.getMarca(),menor.getModelo()))
        return indice
    
    def Mostrar(self,indiceG,indiceE):
        print('Tipo de calefactor: {}'.format(type(self.__arreglo[indiceG])))
        print('\tDatos del calefactor a Gas de menor consumo: ')
        print('\t\tMarca: {} Modelo: {} matricula: {} Calortias:{}'.format(self.__arreglo[indiceG].getMarca(),self.__arreglo[indiceG].getModelo(),self.__arreglo[indiceG].getMatricula(),self.__arreglo[indiceG].getCalorias()))
        print('Tipo de calefactor: {}'.format(type(self.__arreglo[indiceE])))
        print('\tDatos del calefactor a Electrico de menor consumo: ')
        print('\t\tMarca: {} Modelo: {} Potencia: {}'.format(self.__arreglo[indiceE].getMarca(),self.__arreglo[indiceE].getModelo(),self.__arreglo[indiceE].getPotencia()))