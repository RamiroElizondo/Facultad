from __future__ import annotations


class Flores:
    __numero:int = 0
    __nombre:str = ""
    __color:str = ""
    __descripcion: str = ""
    __contador = 0

    def __init__(self, num:int,nom:str,color:str,des:str):
        self.__numero = num
        self.__nombre = nom
        self.__color = color
        self.__descripcion = des
    
    def getNombre(self):
        return self.__nombre
        
    def __str__(self):
        return ('Flor: {} Nombre: {} Color: {} Descrpcion: {}'.format(self.__numero,self.__nombre,self.__color,self.__descripcion))
    
    def contar(self):
        self.__contador += 1
    
    def getContador(self):
        return self.__contador
    
    def __lt__(self,otro:Flores):
        return self.__contador < otro.__contador