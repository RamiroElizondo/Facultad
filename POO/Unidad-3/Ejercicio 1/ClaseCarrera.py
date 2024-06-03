class Carrera:
    __cod: int = 0
    __nombre:str = ""
    __titulo:str = ""
    __duracion:str = ""
    __tipo:str  = ""

    def __init__(self,cod:int, nombre:str, titulo:str, duracion:str, tipo:str):
        self.__cod = cod
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__tipo = tipo
    
    def getDuracion(self):
        return self.__duracion

    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__cod

    def __str__(self):
        return ('Codigo: {} Carrera: {} Titulo: {} Duracion: {} Tipo: {}'.format(self.__cod,self.__nombre,self.__titulo,self.__duracion,self.__tipo))