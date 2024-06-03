from ClaseArtefacto import Artefacto


class Televisor(Artefacto):
    __tipoPantalla:str = ""
    __pulgadas:int = 0
    __tipoDefinicion:str = ""
    __conexionI:bool = False

    def __init__(self,marca,modelo,color,pais,precio,tipoPantalla,pulgada,tipoD,conexion):
        super().__init__(marca,modelo,color,pais,precio)
        self.__tipoPantalla = str(tipoPantalla)
        self.__pulgadas = int(pulgada)
        self.__tipoDefinicion = str(tipoD)
        self.__conexionI = bool(conexion)

    def ImporteVentaT(self):
        venta:float = self.getPrecio()
        if self.__tipoDefinicion == "SD":
            venta = venta + (venta * 0.01)
        elif self.__tipoDefinicion == "HD":
            venta = venta + (venta * 0.02)
        elif self.__tipoDefinicion == "FULLHD":
            venta = venta + (venta * 0.03)
        if self.__conexionI == True:
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
                capacidadL = self.__tipoPantalla,
                velocidad = self.__pulgadas,
                cantidadP = self.__tipoDefinicion,
                tipoC = self.__conexionI
            )
        )
        return d