class ViajeroFrecuente:
    __num_viajero = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = ""

    def __init__(self,num,dni,nombre,apellido,millas):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas
    
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self,millasRecorridas:int):
        self.__millas_acum = self.__millas_acum + millasRecorridas
        return ViajeroFrecuente.cantidadTotalMillas(self)
        #return self.__millas_acum
    
    def canjearMillas(self,cantidad:int):
        if cantidad > self.__millas_acum:
            print('No hay suficientes millas para canjear')
        else: 
            print('Millas Canjeadas')
            self.__millas_acum = self.__millas_acum - cantidad
        return ViajeroFrecuente.cantidadTotalMillas(self)
    
    def getNumero(self):
        return self.__num_viajero
    
    def Mostrar(self):
        return self.__num_viajero + self.__dni + self.__nombre + self.__apellido + self.__millas_acum