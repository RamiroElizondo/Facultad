from __future__ import annotations

class Proyecto:
    __idProyecto:str = ""
    __titulo:str = ""
    __palabrasClaves:str = ""
    __puntaje:int = 0
    def __init__(self, id:str, titulo:str, palabras:str):
        self.__idProyecto = id
        self.__titulo = titulo
        self.__palabrasClaves = palabras
    
    def getIdProyecto(self):
        return self.__idProyecto
    
    def setpuntaje(self,puntaje):
        self.__puntaje = puntaje
    
    def getpuntaje(self):
        return self.__puntaje

    def mostrarProyecto(self):
        return print('Id: -{}- Titulo: -{}- Palabras Claves: -{}- Puntaje: -{}-'.format(self.__idProyecto,self.__titulo,self.__palabrasClaves,self.__puntaje))
    
    def __gt__(self,otro: Proyecto):
        return self.__puntaje > otro.getpuntaje()