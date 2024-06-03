#lista
import csv
from claseProyecto import Proyecto
from operator import attrgetter


class ManejadorProyecto:
    __listaobjetos: list[Proyecto]
    def __init__(self):
        self.__listaobjetos = []
    
    def cargarListaP(self):
        with open("Integrador Optativo\proyectos.csv",'r',encoding='utf8')as archivo:
            reader = csv.reader(archivo,delimiter=';')
            next(reader,None)
            for linea in reader:
                objeto = Proyecto(linea[0],linea[1],linea[2])
                self.__listaobjetos.append(objeto)
    
    def obtener(self):
        lista = []
        for proyecto in self.__listaobjetos:
            lista.append(proyecto.getIdProyecto())
        return lista
    
    def cargarPuntaje(self,listaPuntajes):
        i:int = 0
        for objeto in self.__listaobjetos:
            objeto.setpuntaje(listaPuntajes[i])
            i+=1
    
    def listarMayorMenor(self):
        self.__listaobjetos.sort(key=lambda x:x.getpuntaje(),reverse=True)
        for objeto in self.__listaobjetos:
            objeto.mostrarProyecto()

