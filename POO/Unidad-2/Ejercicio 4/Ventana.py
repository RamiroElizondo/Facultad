class Ventana:
    __titulo = ""
    __supizqX = 0
    __supizqY = 0
    __infderX = 0
    __infderY = 0

    def __init__(self, titulo:str, supizqX: int=0, supizqY:int=0, infderX:int=500, infderY:int=500):
        self.__titulo = titulo
        self.__supizqX = supizqX
        self.__supizqY = supizqY
        self.__infderX = infderX
        self.__infderY = infderY

    def mostrar(self):
        return print('\nPunto Superior ({})({}) Punto Inferior ({})({})\n'.format(self.__supizqX, self.__supizqY, self.__infderX, self.__infderY))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__infderY - self.__supizqY

    def ancho(self):
        return self.__infderX - self.__supizqX

    def moverDerecha(self, movimiento:int):
        supIX:int = self.__supizqX + movimiento
        infIX:int = self.__infderX + movimiento
        if  supIX < 0 or infIX >500:
            print('====El Movimiento sobrepaasara los limites====')
        else:
            print('====Valores Correctos====')
            self.__supizqX = supIX
            self.__infderX = infIX

    def moverIzquierda(self, movimiento:int):
        supIX:int = self.__supizqX - movimiento
        infIX:int = self.__infderX - movimiento
        if  supIX < 0 or infIX >500:
            print('====El Movimiento sobrepaasara los limites====')
        else:
            print('====Valores Correctos====')
            self.__supizqX = supIX
            self.__infderX = infIX

    def subir(self, movimiento:int = 0):
        supIY:int = self.__supizqY - movimiento
        infIY:int = self.__infderY - movimiento
        if  supIY < 0 or infIY >500:
            print('====El Movimiento sobrepaasara los limites====')
        else:
            print('====Valores Correctos====')
            self.__supizqY = supIY
            self.__infderY = infIY

    def bajar(self, movimiento:int = 0):
        supIY:int = self.__supizqY + movimiento
        infIY:int = self.__infderY + movimiento
        if  supIY < 0 or infIY >500:
            print('====El Movimiento sobrepaasara los limites====')
        else:
            print('====Valores Correctos====')
            self.__supizqY = supIY
            self.__infderY = infIY