from zope.interface import interface

class Interfaz(interface):
    def insertarElemento(elemneto, pos:int):
        pass
    
    def agregarElemento(elemento):
        pass

    def mostrarElemento(pos:int):
        pass
