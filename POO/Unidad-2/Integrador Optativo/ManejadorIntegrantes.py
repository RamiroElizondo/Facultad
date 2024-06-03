#arreglo
from errno import ESTALE
from re import I
import numpy
import csv
from claseIntegranteProyecto import Integrante


class ManejadorIntegrante:
    """__areeglobjetos: numpy.array[Integrante]
    def __init__(self):
        with open("Integrador Optativo\integrantesProyecto.csv",'r')as archivo:
            cantidad = len(archivo.readlines())
            self.__areeglobjetos = numpy.empty(cantidad,dtype=Integrante)

    def cargarArregloI(self):
        with open("Integrador Optativo\integrantesProyecto.csv",'r',encoding='utf8')as archivo:
            archivo.seek(0)
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Integrante(linea[0],linea[1],linea[2],linea[3],linea[4])
            numpy.append(self.__areeglobjetos,objeto)
        print(self.__areeglobjetos)
"""
    __arreglobjetos: Integrante
    __lista: list[Integrante]

    def __init__(self):
        self.__lista = []

    def cargarArregloI(self):
        with open("Integrador Optativo\integrantesProyecto.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Integrante(linea[0],linea[1],linea[2],linea[3],linea[4])
                self.__lista.append(objeto)
            self.__areeglobjetos = numpy.array(self.__lista,dtype=Integrante)
    
    def mostrar(self):
        for componente in self.__areeglobjetos:
            componente.mostrarObjeto()

    #Inciso a
    def calcular1(self,proyecto):
        contador:int = 0
        puntos:int = 0
        for objeto in self.__areeglobjetos:
            if proyecto == objeto.getId():
                contador +=1
        if contador >= 3:
            puntos = 10
        else:
            print('<<El proyecto: {} debe tener como minimo 3 integrantes>>'.format(proyecto))
            puntos = -20
        return puntos

    #Inciso b
    def calcular2(self,proyecto):
        i:int = 0
        puntos:int = 0
        bandera = True
        while i < len(self.__areeglobjetos) and bandera == True:
            if self.__areeglobjetos[i].getId() == proyecto:
                if self.__areeglobjetos[i].getRol() == 'Director':
                    if self.__areeglobjetos[i].getCategoria() == 'I' or self.__areeglobjetos[i].getCategoria() == 'II':
                        puntos = 10
                        bandera = False
                    else:
                        print('<<El Director del Proyecto: {} debe tener categoría I o II>>'.format(proyecto))
                        puntos = -5
                        bandera = False
            i+=1
        return puntos
    
    #Inciso c
    def calcular3(self,proyecto):
        i:int = 0
        puntos:int = 0
        bandera = True
        while i < len(self.__areeglobjetos) and bandera == True:
            if self.__areeglobjetos[i].getId() == proyecto:
                if self.__areeglobjetos[i].getRol()== 'Codirector':
                    if self.__areeglobjetos[i].getCategoria() == 'I' or self.__areeglobjetos[i].getCategoria() == 'II' or self.__areeglobjetos[i].getCategoria() == 'III':
                        puntos = 10
                        bandera = False
                    else:
                        print('<<El Codirector del Proyecto: {} debe tener como mínimo categoría III>>'.format(proyecto))
                        puntos = -5
                        bandera = False
            i+=1
        return puntos
    
    #Inciso d
    def calcular4(self,proyecto):
        i = 0
        valor = False
        bandera = True
        while i < len(self.__areeglobjetos) and bandera == True:
            if self.__areeglobjetos[i].getId() == proyecto:
                if self.__areeglobjetos[i].getRol()== 'Director':
                    valor = True
                    bandera = False
                else:
                    valor = False
            i+=1
        return valor
    #Inciso e
    def calcular5(self,proyecto):
        i = 0
        valor = False
        bandera = True
        while i < len(self.__areeglobjetos) and bandera == True:
            if self.__areeglobjetos[i].getId() == proyecto:
                if self.__areeglobjetos[i].getRol()== 'Codirector':
                    valor = True
                    bandera = False   
                else:
                    valor = False
            i+=1
        return valor
    
