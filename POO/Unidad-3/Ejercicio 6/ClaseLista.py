from zope.interface import implementer
from ClaseInterfaz import Interfaz
from ClaseNodo import Nodo
import json
from ClaseArtefacto import Artefacto
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa

@implementer(Interfaz)
class ListaEnlazada:
    __comienzo: Nodo | None
    def __init__(self):
        self.__comienzo = None

    def agregar(self, elemento):
        nuevoNodo = Nodo(elemento)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevoNodo

    def size(self):
        contador = 0
        actual = self.__comienzo
        while actual is not None:
            contador += 1
            actual = actual.getSiguiente()
        return contador

    def insertarElemento(self, elemento, posicion): # Insertar en una posicion especifica
        posicion = posicion - 1
        if posicion > self.size() - 1:
            print ("Fuera de Rango")
            raise IndexError
        actual = self.__comienzo
        previo = None
        pos = 0
        if posicion is 0:
            self.agregar(elemento)
        else:
            nuevoNodo = Nodo(elemento)
            while pos < posicion:
                pos += 1
                previo = actual
                actual = actual.getSiguiente() #type: ignore
            previo.setSiguiente(nuevoNodo) #type: ignore
            nuevoNodo.setSiguiente(actual)
    
    def agregarElemento(self, elemento): # Agregar al final
        actual = self.__comienzo
        previo = None
        pos = 0
        tamaño = self.size()
        while pos < tamaño:
            previo = actual
            actual = actual.getSiguiente() #type: ignore
            pos += 1
        nuevoNodo = Nodo(elemento)
        if previo is None:
            nuevoNodo.setSiguiente(actual)
            self.__comienzo = nuevoNodo
        else:
            previo.setSiguiente(nuevoNodo)
    
    def mostrarLista(self):
        actual = self.__comienzo
        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()
    
    def mostrarposicion(self,pos:int):
        pos = pos -1 
        actual = self.__comienzo
        indice = 0
        bandera = False
        while actual != None and bandera == False:
            if indice == pos:
                print('Elemento Encontrado: ')
                print(f'Tipo: {type(actual.getDato())}')
                bandera = True
            indice += 1
        
        if indice > self.size():
            print('Elemento no encontrado')
    
    def contar(self):
        contadores = [0,0,0]
        actual = self.__comienzo
        while actual != None:
            if actual.getDato().getMarca() == "Philips":
                tipo = type(actual.getDato())
                if tipo == Heladera:
                    contadores[0] += 1
                elif tipo == Lavarropa:
                    contadores[1] += 1
                elif tipo == Televisor:
                    contadores[2] += 1
            actual = actual.getSiguiente()
        print('Hay {} Heladeras, {} Lavarropas y {} Televisores marca Philips'.format(contadores[0],contadores[1],contadores[2]))
    
    def mostrarMarcaLavarropa(self):
        actual = self.__comienzo
        while actual != None:
            if type(actual.getDato())== Lavarropa:
                if actual.getDato().getTicoC() == "Superior":
                    print(actual.getDato().getMarca())
            actual = actual.getSiguiente()

    def mostrarDatosVenta(self):
        actual = self.__comienzo
        importeVenta:float = 0.0
        print('Marca\t\tPais de Origen\t\tImporte de Venta')
        while actual != None:
            if type(actual.getDato()) == Lavarropa:
                importeVenta = actual.getDato().ImporteVentaL()
            elif type(actual.getDato()) == Heladera:
                importeVenta = actual.getDato().ImporteVentaH()
            elif type(actual.getDato()) == Televisor:
                importeVenta = actual.getDato().ImporteVentaT()
            print('%s%22s%25.2f'%(actual.getDato().getMarca(),actual.getDato().getPais(),importeVenta))
            actual = actual.getSiguiente()
    
    def getComienzo(self):
        return self.__comienzo
    
    def __iter__(self):
        actual = self.__comienzo
        while actual != None:
            yield actual.getDato()
            actual = actual.getSiguiente()

