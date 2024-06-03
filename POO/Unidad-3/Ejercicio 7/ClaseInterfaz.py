from zope.interface import Interface

class Interfaz(Interface):#type: ignore
    def insertarElemento(self,elemento,pos):
        pass

    def agregarElemento(self,elemento):
        pass

    def mostrarElemento(self,pos):
        pass