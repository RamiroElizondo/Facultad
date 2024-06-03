class Direccion:
    def __init__(self, calle, numero, ciudad):
        self.__calle = calle
        self.__numero = numero
        self.__ciudad = ciudad

    def getValores(self):
        return self.__calle + ' Numero: ' + self.__numero + ' ' + self.__ciudad

class Persona:
    __direccion = None
    
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
    
    def __str__(self):
        return 'Nombre: ' + self.__nombre + self.__direccion.getValores()

dir1 = Direccion("Calle: 1", "123", "Ciudad: 1")
persona1 = Persona("Juan ", dir1)

dir2 = Direccion("Calle 2", "456", "Ciudad 2")
persona2 = Persona("Maria", dir2)

print(persona1)

"""
La agregación ocurre cuando una clase tiene una relación "tiene un" con otra clase. En este ejemplo, tenemos dos clases, Persona y Direccion. 
La clase Persona tiene una instancia de la clase Direccion, pero la instancia de la clase Direccion puede ser compartida por otras clases.

En este ejemplo, las clases Persona y Direccion tienen una relación de agregación, donde Persona tiene una instancia de Direccion.
La instancia de Direccion puede ser compartida por otras clases, lo que hace que este ejemplo sea un ejemplo de agregación.
"""