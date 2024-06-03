class Jugador:
    __nombre:str = ""
    __dni:str = ""
    __ciudadN:str = ""
    __pais:str = ""
    __fechaN:str = ""
    
    def __init__(self, nom, dni, ciudadN, pais, fechaN):
        self.__nombre = str(nom)
        self.__dni = str(dni)
        self.__cuidadN = str(ciudadN)
        self.__pais = str(pais)
        self.__fechaN = str(fechaN)
    
    def __str__(self):
        return ('Nombre: {} Dni: {} CiudadN: {} Pais: {} FechaN: {}'.format(self.__nombre,self.__dni,self.__cuidadN,self.__pais,self.__fechaN))
    
    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def str(self):
        return ('Nombre: {} Dni: {} CiudadN: {} Pais: {} FechaN: {}'.format(self.__nombre,self.__dni,self.__cuidadN,self.__pais,self.__fechaN))
