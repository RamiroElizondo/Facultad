class Palindromo:
    __palabra = None

    def __init__(self,palabra):
        self.__palabra = palabra
    
    def esPalindromo(self):
        i:int = 0
        j:int = -len(self.__palabra)
        bandera = True
        while i < abs(j) and bandera:
            if self.__palabra[i] != self.__palabra[j]:
                bandera = False
            else:
                i+=1
                j+=1

        return bandera
    
    def setPalabra(self,nuevaPalabra):
        self.__palabra = nuevaPalabra