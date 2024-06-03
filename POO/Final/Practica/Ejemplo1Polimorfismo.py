class Animal:
    __nombre:str = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Gato(Animal):

    def __init__(self,nombre):
        super().__init__(nombre)

    def hablar(self):
        return 'Meow!'

class Perro(Animal):

    def __init__(self,nombre):
        super().__init__(nombre)

    def hablar(self):
        return 'Woof!'

def main():
    animales = [Gato('Missy'),
               Perro('Rocky'),
               Gato('Mittens')]

    for animal in animales:
        print(f"{animal.nombre} dice {animal.hablar()}")

if __name__ == '__main__':
    main()

"""
En este ejemplo, tenemos una clase base Animal con un método hablar() 
que no hace nada. Luego, tenemos dos clases hijas Gato y Perro que heredan 
de Animal y redefinen el método hablar() para que devuelvan una cadena de 
sonido diferente para cada animal.

En la función main(), creamos una lista de objetos Gato y Perro y los 
recorremos. Cuando llamamos a animal.hablar(), la forma específica de
la clase se utiliza para determinar qué método hablar() se ejecutará.
En otras palabras, la misma llamada a hablar() produce resultados 
diferentes dependiendo del tipo de objeto que se encuentra en la lista.

Este es un ejemplo típico de polimorfismo, donde una llamada a un método
en un objeto es polimórfica y produce resultados diferentes dependiendo
de la forma específica del objeto.
"""
