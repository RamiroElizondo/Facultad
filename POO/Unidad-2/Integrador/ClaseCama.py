
class Cama:
    __idCama: int = 0
    __habitacion: int = 0
    __estado:bool = False
    __nya: str = None
    __diagnostico: str = None
    __fechainternacion: str = ""
    __fechaalta: str = ""

    def __init__(self, idCama: int, habitacion: int, estado: bool, nya: str, diagnostico: str, fechainternacion: str, fechaalta: str):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__nya = nya
        self.__diagnostico = diagnostico
        self.__fechainternacion = fechainternacion
        self.__fechaalta = fechaalta
    
    def getIdCama(self):
        return self.__idCama

    def getEstado(self):
        return self.__estado
        
    def getnya(self):
        return self.__nya

    def getDiagnostico(self):
        return self.__diagnostico

    def setFechaAlta(self, fecha):
        self.__fechaalta = fecha

    def mostrarPaciente(self):
        return print("""
        Paciente: %s \tCama: %s \tHabitacion: %d
        Diagnostico: %s \tFecha de Internacion: %s
        Fecha de Alta: %s """
        % (self.__nya, self.__idCama, self.__habitacion, self.__diagnostico, self.__fechainternacion, self.__fechaalta))
        