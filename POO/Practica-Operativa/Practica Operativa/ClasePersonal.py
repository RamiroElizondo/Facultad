from __future__ import annotations


class Personal:
    __legajo:int = 0
    __dni:str = ""
    __apellido:str = ""
    __nombre:str = ""
    __sueldo:int = 0
    __sueldoLiquidar:int = 0

    def __init__(self,legajo:int,dni:str,apellido:str,nombre:str,sueldo:int):
        self.__legajo = legajo
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo = sueldo
        self.__sueldoLiquidar = sueldo

    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni

    def getLegajo(self):
        return self.__legajo
    
    def getSueldo(self):
        return self.__sueldo
    
    def getSueldoLCadena(self):
        sueldo = str(self.__sueldoLiquidar)
        return '$'+sueldo

    def getSueldoL(self):
        return self.__sueldoLiquidar

    def CalcularSueldoL(self,valor,cod):
        if cod == 'A':
            self.__sueldoLiquidar = self.__sueldoLiquidar + valor #Suma Adicional
        elif cod == 'D':
            self.__sueldoLiquidar = self.__sueldoLiquidar - valor # Resta Descuento
        return self.__sueldoLiquidar

    def __gt__(self,otro:Personal):
        if type(otro) != Personal:
            raise Exception('Error mayor')
        valor = False
        if self.__apellido == otro.__apellido:
            if self.__nombre > self.__nombre:
                valor = True
        elif self.__apellido > otro.__apellido:
            valor = True
        return valor

    def __lt__(self,otro):
        if type(otro) != int:
            raise Exception('Error menor')
        return self.__sueldoLiquidar < otro
    
    def __str__(self):
        return ('Legajo: {} DNI: {} Apellido: {} Nombre: {} Sueldo: {}'.format(self.__legajo,self.__dni,self.__apellido,self.__nombre,self.__sueldo))
        

