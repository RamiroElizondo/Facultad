class Carrera:
    __titulo:str 
    __cantAños:int
    __libroRecibidos = []

    def __init__(self,titulo="",años=0):
        self.__titulo = titulo
        self.__cantAños = años
    
    def completarLibro(self,persona,fecha):
        registro = Registro(fecha,self,persona)
        self.__libroRecibidos.append(registro)

    def mostrarRegistros(self):
        for registro in self.__libroRecibidos:
            print(registro)

    def __str__(self):
        return 'Su titulo'
class Persona:
    __nombre:str
    __apellido:str

    def __init__(self,nombre="",apellido=""):
        self.__nombre = nombre
        self.__apellido = apellido

class Registro:
    __fechaEgreso = ""
    __carrera = None
    __persona = None

    def __init__(self,egreso,carrera,persona):
        self.__fechaEgreso = egreso
        self.__carrera = carrera
        self.__persona = persona
    
    def __str__(self):
        cadena = 'Fecha Egreso'
        return cadena

if __name__ == '__main__':
    carrera = Carrera('Licenciado en Sistemas de Informacion',5)
    persona = Persona('Ramiro','Elizondo')
    carrera.completarLibro(persona, '20/11/25')
    carrera.mostrarRegistros()