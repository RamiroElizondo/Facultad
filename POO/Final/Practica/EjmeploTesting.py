import unittest

class Calculadora:
    __a:int
    __b:int
    def __init__(self,a=None,b=None):
        self.__a = a
        self.__b = b
        
    def sumar(self):
        return self.__a + self.__b

    def restar(self):
        return self.__a - self.__b

    def multiplicar(self):
        return self.__a * self.__b

    def dividir(self):
        return self.__a / self.__b

class TestCalculadora(unittest.TestCase):
    __calc = None
    def setUp(self):
        self.__calc = Calculadora(10,5)

    def test_sumar(self):
        self.assertEqual(self.__calc.sumar(), 15)

    def test_restar(self):
        self.assertEqual(self.__calc.restar(), 5)

    def test_multiplicar(self):
        self.assertEqual(self.__calc.multiplicar(), 50)

    def test_dividir(self):
        self.assertEqual(self.__calc.dividir(), 2)

if __name__ == '__main__':
    unittest.main()

"""
En este ejemplo, la clase "Calculadora" tiene métodos para sumar, restar, multiplicar y dividir dos números. 
Luego, se crean pruebas de unidad para cada uno de estos métodos usando la clase "unittest" de Python.

En las pruebas de unidad, se crea una instancia de la clase "Calculadora" en el método "setUp" para que pueda 
ser utilizada en cada una de las pruebas. Luego, se llama a cada método de la clase "Calculadora" y se verifica 
que el resultado sea el esperado usando la función "assertEqual".

Para ejecutar las pruebas, simplemente se llama a la función "unittest.main()". Si todas las pruebas pasan, 
deberías ver una salida similar a la siguiente:
"""