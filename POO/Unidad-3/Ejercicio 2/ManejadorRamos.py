import numpy
from ClaseRamo import Ramo
from ManejadorFlores import ManejadorFlores


class ManejadorRamos:
    __listaRamos: list[Ramo]

    def __init__(self):
        self.__listaRamos = []

    def AsignarT(self,tamaño)->int:
        valor:int = 0
        if tamaño == 'Chico':
            valor = 1
        elif tamaño == 'Mediano':
            valor = 2
        elif tamaño == 'Grande':
            valor = 4
        return valor

    def cargarRamos(self,valor:int,tamaño):
        i:int = 1
        listaR = []
        objeto = Ramo(tamaño)
        while i <= valor:
            flor = input('Ingrese nombre de la flor {} a Agregar (Termina con Fin): '.format(i))
            objeto.addRamor(flor)
            i+=1
        self.__listaRamos.append(objeto)
    
    def maspedidas(self,arreglo):
        lista = []
        for flor in arreglo:
            for ramo in self.__listaRamos:
                for linea in ramo.getlistaRamo():
                    if flor.getNombre() == linea:
                        flor.contar()
        i:int = 0
        """for objeto in arreglo:
            print('Flor {} Contador {}'.format(objeto.getNombre(),objeto.getContador()))
            i+=1"""
        arregloR = numpy.sort(arreglo)[::-1]
        while i < 5:
            print('Flor {} Contador {}'.format(arregloR[i].getNombre(),arregloR[i].getContador()))
            i+=1
        
    def mostrarTipo(self,tipo:str):
        print('Flores:\n')
        for ramo in self.__listaRamos:
            if ramo.getTamaño() == tipo:
                for linea in ramo.getlistaRamo():
                    print(linea)

    """def mostrar(self):
        i:int = 1
        for objeto in self.__listaRamos:
            print('Flores del Ramo {}'.format(i))
            print('Tamaño: {} \nFlores: {}'.format(objeto.getTamaño(),objeto.getlistaRamo()))
            i+=1"""
