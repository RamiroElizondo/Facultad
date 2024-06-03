class Novedades:
    __legajo:int = 0
    __importe:int = 0
    __concepto:str = 0
    __codigo:str = 0

    def __init__(self,legajo:int,importe:int,concepto:str,codigo:str):
        self.__legajo = legajo
        self.__importe = importe
        self.__concepto = concepto
        self.__codigo = codigo
    
    def getImporte(self):
        return self.__importe
    
    def getCodigo(self):
        return self.__codigo
    
    def getLegajo(self):
        return self.__legajo
    
    def getConcepto(self):
        return self.__concepto
    
    def getImporteCadena(self):
        importe = str(self.__importe)
        return ' $'+importe
    
    def __str__(self):
        return ('Legajo: {} Importe: {} Concepto: {} Codigo: {}'.format(self.__legajo,self.__importe,self.__concepto,self.__codigo))
