class Medicamento:
    __idCama:int = 0
    __idMedicamento:int = 0
    __nombreM:str = ""
    __monodroga:str = ""
    __presentacion:str = ""
    __cantidadAplicada:int = 0
    __precioTotal:int = ""

    def __init__(self, idCama:int, idMedicamento:int, nombreM:str, monodroga:str, presentacion:str, cantidadAplicada:int, precioTotal:int):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombreM = nombreM
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidadAplicada = cantidadAplicada
        self.__precioTotal = precioTotal

    def getIdcama(self):
        return self.__idCama

    def getNombreM(self):
        return self.__nombreM

    def getMonodroga(self):
        return self.__monodroga

    def getPresentacion(self):
        return self.__presentacion

    def getCantidadAplicada(self):
        return self.__cantidadAplicada

    def getprecioTotal(self):
        return self.__precioTotal
