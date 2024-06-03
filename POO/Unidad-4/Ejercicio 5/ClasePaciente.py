class Paciente:
    __nombre: str = ""
    __apellido:str = "" 
    __telefono: str = ""
    __altura: float = 0.0
    __peso: float = 0.0

    def __init__(self, nombre: str, apellido: str, telefono: str, altura: float, peso: float):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__altura = float(altura)
        self.__peso = float(peso)

    def __str__(self):
        return f"{self.__nombre} {self.__apellido}"

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def toJson(self):
        d=dict(
            nombre=self.__nombre,
            apellido=self.__apellido,
            telefono=self.__telefono,
            altura=self.__altura,
            peso=self.__peso
        )
        return d
    
    def calcularMCI(self):
        lista = []
        valor = self.__peso / ((self.__altura / 100) ** 2)
        cadena = ""
        if valor < 18.5:
            cadena = "Peso inferior al normal"
        elif  18.5 <= valor < 25:
            cadena = "Peso normal"
        elif 25 <= valor < 30:
            cadena = "Peso superior al normal"
        else:
            valor = "Obesidad"
        lista.append(valor)
        lista.append(cadena)
        print(lista)
        return lista
