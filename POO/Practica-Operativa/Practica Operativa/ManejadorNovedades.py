import csv
from ClaseNovedad import Novedades


class ManejadorNovedades:
    __listaobjetos: list[Novedades]
    def __init__(self):
        self.__listaobjetos = []

    """def cargarNovedades(self,arreglo):
        i:int = 0
        
        with open("novedades.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';') 
            next(reader,None)
            for linea in reader:
                objeto = Novedades(int(linea[0]),int(linea[1]),linea[2],linea[3])
                self.__listaobjetos.append(objeto)
                
        for objeto in self.__listaobjetos:
            print(objeto)"""
    
    def cargarNovedades(self,manP):
        arreglo = manP.getArreglo()
        with open("Practica Operativa\\novedades.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';') 
            next(reader,None)
            for linea in reader:
                bandera = False
                i:int = 0
                while i < len(arreglo) and bandera == False:
                    bandera = False
                    if int(linea[0]) == arreglo[i].getLegajo():
                        objeto = Novedades(int(linea[0]),int(linea[1]),linea[2],linea[3])
                        self.__listaobjetos.append(objeto)
                        bandera = True
                    i+=1
        """print('\n')
        for objeto in self.__listaobjetos:
            print(objeto)"""
    
    def getLista(self):
        return self.__listaobjetos
                