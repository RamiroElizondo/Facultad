import csv 
import numpy
from ClaseCama import Cama


class ManejadorCama:
    __listaobjetos: Cama

    def __init__(self):
        with open("Integrador\camas.csv", 'r') as archivo:
            lista: list[Cama] = []
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Cama(int(linea[0]),int(linea[1]),bool(linea[2]),linea[3],linea[4],linea[5],linea[6])
                lista.append(objeto)
            self.__listaobjetos = numpy.array(lista,dtype=Cama)

    def buscarMostrar(self, nombre):
        i:int = 0
        valor:int = 0
        while  i < len(self.__listaobjetos) and nombre != self.__listaobjetos[i].getnya():
            i += 1
        else:
            if i < len(self.__listaobjetos):
                fechaA = input('Ingrese Fecha de Alta: ')
                valor = self.__listaobjetos[i].getIdCama()
                self.__listaobjetos[i].setFechaAlta(fechaA)
                self.__listaobjetos[i].mostrarPaciente()
            else: 
                print('Paciente no encontrado'.center(30, '-'))
        return valor
    
    def listar(self, diagnostico):
        for objeto in self.__listaobjetos:
            if objeto.getEstado() == True:
                if diagnostico == objeto.getDiagnostico():
                    objeto.mostrarPaciente()

