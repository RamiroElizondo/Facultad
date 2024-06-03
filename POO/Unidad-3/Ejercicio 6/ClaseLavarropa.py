from ClaseArtefacto import Artefacto

class Lavarropa(Artefacto):
    __capacidadL:int = 0
    __velocidad:int = 0
    __cantidadP: int = 0
    __tipoC:str = ""

    def __init__(self,marca,modelo,color,pais,precio,cap,vel,cant,tipo):
        super().__init__(marca,modelo,color,pais,precio)
        self.__cantidadL = int(cap)
        self.__velocidad = int(vel)
        self.__cantidadP = int(cant)
        self.__tipoC = str(tipo)
    
    def getTicoC(self):
        return self.__tipoC

    def ImporteVentaL(self):
        venta:float = self.getPrecio()
        if self.__capacidadL <= 5:
            venta = venta + (venta * 0.01) 
        elif self.__capacidadL > 5:
            venta = venta + (venta * 0.05)
        return venta
    
    def toJson(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precio = self.getPrecio(),
                capacidadL = self.__capacidadL,
                velocidad = self.__velocidad,
                cantidadP = self.__cantidadP,
                tipoC = self.__tipoC
            )
        )
        return d