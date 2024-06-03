from ClaseFacultad import Facultad
import csv

class ManejadorFacultad:
    __listaFacultad: list[Facultad]

    def __init__(self):
        self.__listaFacultad = []
    
    def cargarFacultades(self):
        with open("facultades.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=',')
            codigo:int = 0
            for linea in reader:
                if codigo == int(linea[0]):
                    self.__listaFacultad[codigo-1].agregarCarrera(linea)
                else:
                    codigo = int(linea[0])
                    objeto = Facultad(int(linea[0]),linea[1],linea[2],linea[3]+' '+linea[4],linea[5])
                    self.__listaFacultad.append(objeto)

    def buscarFacultad(self, cod):
        i:int = 0
        bandera = False
        print(len(self.__listaFacultad))
        while i < len(self.__listaFacultad) and bandera == False:
            if self.__listaFacultad[i].getCodigo() == cod:
                print(self.__listaFacultad[i].getNombre())
                self.__listaFacultad[i].retornarvalores()
                bandera = True
            i+=1
    
    def buscarCarrera(self,carrera):
        i:int = 0
        j:int = 0
        bandera = False
        while i < len(self.__listaFacultad) and bandera == False:
            valores = self.__listaFacultad[i].buscarigual(carrera)
            if valores[1] == True:
                print('Nombre {} Localidad: {}'.format(self.__listaFacultad[i].getNombre(),self.__listaFacultad[i].getLocalidad()))
                print('Codigo Carrera: -{}- -{}-'.format(self.__listaFacultad[i].getCodigo(),valores[0]))
                bandera = True
            i+=1
