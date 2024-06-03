class Pago:
    __fecha:str = ""
    __monto:int = 0

    def __init__(self,fecha,monto):
        self.__fecha = fecha
        self.__monto = monto
    
    def mostrar_detalles(self):
        pass

    def getFecha(self):
        return self.__fecha

    def getMonto(self):
        return self.__monto