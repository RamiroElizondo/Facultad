from Pago import Pago
class Empleado:
    __nombre: str = ""
    __apellido:str = ""
    __salario:int = 0
    __lista:Pago = []

    def __init__(self,nombre,apellido,salario):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = salario
    
    def getNombre(self):
        return self.__nombre

    def pagoSueldo(self,pago):
        self.__lista.append(pago)
    
    def getApellido(self):
        return self.__apellido
    
    def getLista(self):
        return self.__lista
