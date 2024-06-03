from ClaseArtefacto import Artefacto


class Heladera(Artefacto):
    __capacidad:int = 0
    __freezer:bool = False
    __ciclica:bool = False

    def __init__(self,marca,modelo,color,pais,precio,cap,freezer,ciclica):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidad = int(cap)
        self.__freezer = bool(freezer)
        self.__ciclica = bool(ciclica)
    
    def ImporteVentaH(self):
        venta:float = self.getPrecio()
        if self.__freezer == False:
            venta = venta + (venta * 0.01)
        elif self.__freezer == True:
            venta = venta + (venta * 0.05)
        if self.__ciclica == True:
            venta = venta + (venta * 0.10)
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
                capacidadL = self.__capacidad,
                velocidad = self.__freezer,
                cantidadP = self.__ciclica
            )
        )
        return d