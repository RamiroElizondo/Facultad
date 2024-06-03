class Motor:
    def __init__(self, tipo,numero):
        self.__tipo = tipo
        self.__numero= numero
class Vidrio():
    def __init__(self,tipoVidrio,numeroSerie):
        self.__tipoVidrio = tipoVidrio
        self.__numeroSerie = numeroSerie

class Auto:
    def __init__(self, marca, modelo, dominio,tipo_motor,numero):
        self.__marca = marca
        self.__modelo = modelo
        self.__dominio = dominio
        self.__motor = Motor(tipo_motor,numero)
        self.__vidrio = Vidrio('Blindado',dominio)

auto1 = Auto("Ford", "Mustang", 'XGF 997', "V8",'UGA 008 992')

"""
La composición ocurre cuando una clase tiene una relación "compuesta por" con otra clase. En este ejemplo, tenemos dos clases, Auto y Motor.
La clase Auto está compuesta por una instancia de la clase Motor. La instancia de la clase Motor solo puede pertenecer a una instancia de la clase Auto.

El motor de un auto legalmente no se puede colocar en otro debido a que tiene un numero que corresponde a ese auto.
Lo mismo pasa con los vidrios del auto, estos tienen grabado el dominio del mismo
"""
