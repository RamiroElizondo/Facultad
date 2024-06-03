from ClasePersonal import Personal

class Nodo:
    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None

    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self,dato):
        self.__siguiente = dato