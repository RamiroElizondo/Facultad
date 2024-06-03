class Artefacto:
    __marca:str = ""
    __modelo:str = ""
    __color:str = ""
    __pais:str = ""
    __precio:float = 0.0

    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca = str(marca)
        self.__modelo = str(modelo)
        self.__color = str(color)
        self.__pais = str(pais)
        self.__precio = float(precio)
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color

    def getPais(self):
        return self.__pais

    def getPrecio(self):
        return self.__precio