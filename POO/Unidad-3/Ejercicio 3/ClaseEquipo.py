class Equipo:
    __nombre: str = ""
    __cuidad: str = ""
    
    def __init__(self,nom,cuidad):
        self.__nombre = str(nom)
        self.__cuidad = str(cuidad)
    
    def __str__(self):
        return ('Nombre: {} Ciudad: {}'.format(self.__nombre,self.__cuidad))

    def getNombre(self):
        return self.__nombre