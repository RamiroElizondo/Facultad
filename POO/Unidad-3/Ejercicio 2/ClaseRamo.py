class Ramo:
    __tamaño:str = ""
    __listaFlores:list

    def __init__(self,tamaño:str):
        self.__tamaño = tamaño
        self.__listaFlores = []
    
    def addRamor(self,ramo):
        self.__listaFlores.append(ramo)
    
    def getTamaño(self)->str:
        return self.__tamaño
    
    def getlistaRamo(self):
        return self.__listaFlores
    
    def __str__(self):
        return ('Tamaño: {} Lista: {}'.format(self.__tamaño,self.__listaFlores))

        #264 422 0531
        #264 545 4931
