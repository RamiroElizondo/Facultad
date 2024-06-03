import csv
import numpy
from ClasePersonal import Personal


class ManejadorPersonal():
    __arreglo: None
    def __init__(self):
        self.__arreglo = numpy.empty(4,dtype=Personal)

    def cargarArreglo(self):
        with open("Practica Operativa\personal.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            i:int=0
            for linea in reader:
                if i == len(self.__arreglo):
                    self.__arreglo.resize(5,dtype=Personal)
                objeto = Personal(int(linea[0]),linea[1],linea[2],linea[3],int(linea[4]))
                self.__arreglo[i] = objeto
                i+=1
            print(len(self.__arreglo))
            

        """for objeto in self.__arreglo:
            print(objeto)
            print('\n')"""

    def calcularSueldos(self,manN):
        lista = manN.getLista()
        for objetoP in self.__arreglo:
            for objetoN in lista:
                if objetoP.getLegajo() == objetoN.getLegajo():
                    cod = objetoN.getCodigo()
                    valor = objetoN.getImporte()
                    sueldo = objetoP.CalcularSueldoL(valor,cod)


    def getArreglo(self):
        return self.__arreglo
    
    def buscaLegajo(self,numero,manN):
        indiceP:int = 0
        valor:int = 0
        bandera1 = False
        lista = manN.getLista()
        while indiceP < len(self.__arreglo) and bandera1 == False:
            if numero == self.__arreglo[indiceP].getLegajo():
                print('Su sueldo a liquidar es: {}'.format(self.__arreglo))
                bandera1 = True
            indiceP+=1

    def ordenar(self,arreglo):
        k:int =1
        i:int
        aux:Personal
        cota:int
        cota= len(arreglo)-1
        while k != -1:
            k=-1
            for i in range(0,cota):
                if arreglo[i] > arreglo[i+1]:
                    aux = arreglo[i]
                    arreglo[i] = arreglo[i+1]
                    arreglo[i+1] = aux
                    k = i
            cota = k 
        return arreglo

    def listado(self,manN):
        i:int = 0
        lista = manN.getLista()
        self.__arreglo = self.ordenar(self.__arreglo)
        #listaT.sort()
        #self.__arreglo = numpy.sort(self.__arreglo)
        for objeto in self.__arreglo:
            print('\n')
            print('Apellido: {:20}Nombre: {}\nDni: {}\nSueldo Basico: {}'.format(objeto.getApellido(),objeto.getNombre(),objeto.getDNI(),objeto.getSueldo()))
            print('Codigo \t\t\tConcepto \t\tImporte')
            for novedad in lista:
                if objeto.getLegajo() == novedad.getLegajo():
                    print('%s %30s %22s'%(novedad.getCodigo(),novedad.getConcepto(),novedad.getImporteCadena()))
            print('Total a Cobrar: {}'.format(objeto.getSueldoLCadena()))

    def buscarMenor(self):
        minimo:int = 1000000
        i:int = 0
        bandera = False
        for objeto in self.__arreglo:
            print(minimo)
            if objeto < minimo:
                minimo = int(objeto.getSueldoL())
        while i < self.__arreglo and bandera == False:
            if minimo == self.__arreglo[i].getSueldoL():
                print('El Sueldo a Cobrar mas bajo es: {}'.format(minimo.getSueldoL()))