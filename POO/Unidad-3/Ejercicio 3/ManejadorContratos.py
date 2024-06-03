import numpy
import pandas as pd
import csv
from datetime import datetime
from ClaseContrato import Contrato


class ManejadorContratos:
    __arreglo: numpy.ndarray

    def __init__(self):
        self.__arreglo = numpy.empty(0,dtype=Contrato)

    def buscarE(self,lista,equipo:str)->list:
        i:int = 0
        bandera = False
        valores = []
        while i < len(lista) and bandera == False:
            if lista[i].getNombre() == equipo:
                print('El equipo existe')
                bandera = True
                valores.append(bandera)
                valores.append(i)
            i+=1
        return valores

    def hacercontrato(self,manJ,manE):
        lista = manJ.getListaJ()
        arreglo = manE.getEquipos()
        for jugador in lista:
            valor = input('Jugador {} Contrado SI - NO: '.format(jugador.getNombre()))
            if valor.upper() == 'SI':
                equipo = input('Equipo? ')
                valores = self.buscarE(arreglo,equipo)
                if valores[0] == True:
                    pago = int(input('Pago Mensual: '))
                    fInicio = input('Fecha inicio: ')
                    fFin = input('Fecha Fin: ')
                    objeto = Contrato(fInicio,fFin,pago,jugador,arreglo[valores[1]])
                    self.__arreglo = numpy.append(self.__arreglo,objeto) #type: ignore
                else:
                    print('El equipo no existe')

    def buscarJugador(self,dni):
        i:int = 0
        bandera = False
        while i < len(self.__arreglo) and bandera == False:
            if dni == self.__arreglo[i].getJugador().getDni():
                print('Esta Contrado')
                print('Equipo: {}'.format(self.__arreglo[i].getEquipo()))
                print('Fecha de Finalizacion: {}'.format(self.__arreglo[i].getFechaFin()))
                bandera = True
            i+=1
        if i > len(self.__arreglo):
            print('Jugador no Contrado')

    def calcular(self,fechaFin,fechaHoy):
        return (fechaFin.year - fechaHoy.year) * 12 + fechaFin.month - fechaHoy.month
    
    def consultarContrato(self,nombre,manE):
        #fechaactual = time.strftime('%d/%m/%Y')
        valor = self.buscarE(manE.getEquipos(),nombre)
        fechaactual = datetime.now()
        if valor[0] == True:
            for objeto in self.__arreglo:
                if objeto.getEquipo().getNombre() == nombre:
                    tiempoRestante = self.calcular(pd.to_datetime(objeto.getFechaFin()),pd.to_datetime(fechaactual))
                    if tiempoRestante == 6:
                        print(objeto.getJugador())
                    else:
                        print('No hay contratos cuyo vencimiento sea en 6 meses')
        else:
            print('El equipo no existe')
    
    def obtenerImporte(self,equipo,manE):
        importe = 0
        valor = self.buscarE(manE.getEquipos(),equipo)
        if valor[0] == True:
            for objeto in self.__arreglo:
                if objeto.getEquipo().getNombre() == equipo:
                    importe = importe + objeto.getPago()
            print('El importe Total de los Contratos: {}'.format(importe))
        else:
            print('El equipo no existe')
    
    def guardarContratos(self):
        with open('Contratos.csv','w') as archivo:
            for objeto in self.__arreglo:
                escritor = csv.writer(archivo)
                escritor.writerows([objeto.getJugador().getDni(),objeto.getEquipo().getNombre(),str(objeto.getFechaInicio()),str(objeto.getFechaFin()),str(objeto.getPago())])