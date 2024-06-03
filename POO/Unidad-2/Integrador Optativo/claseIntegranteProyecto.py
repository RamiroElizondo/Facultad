from time import strftime


class Integrante:
    __idProyecto:str = ""
    __nombre:str = ""
    __dni:str = ""
    __categoria:str= ""
    __rol:str = ""
    def __init__(self, id:str, nombre:str, dni:str, categoria:str, rol: str ):
        self.__idProyecto = id
        self.__nombre = nombre
        self.__dni = dni
        self.__categoria = categoria
        self.__rol = rol

    def mostrarObjeto(self):
        return print(f'Id: {self.__idProyecto} Nombre: {self.__nombre} DNI: {self.__dni} Categoria: {self.__categoria} Rol: {self.__rol}')
    def getId(self):
        return self.__idProyecto
    
    def getCategoria(self):
        return self.__categoria
    
    def getRol(self):
        return self.__rol