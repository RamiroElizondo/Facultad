from ClaseCarrera import Carrera


class Facultad:
    __codF:int = 0
    __nombreF:str = ""
    __direccion:str = ""
    __localidad:str = ""
    __telefono:str = ""
    __listaCarrera: list[Carrera]

    def __init__(self, cod:int, nombre:str, direccion:str, localidad:str, telofono:str):
        self.__codF = cod
        self.__nombreF = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telofono
        self.__listaCarrera = []
    
    def agregarCarrera(self,linea):
        objeto = Carrera(int(linea[1]),linea[2],linea[3],linea[4],linea[5])
        self.__listaCarrera.append(objeto)
    
    def getlista(self):
        return self.__listaCarrera
    
    def getCodigo(self):
        return self.__codF

    def getNombre(self):
        return self.__nombreF
    
    def getLocalidad(self):
        return self.__localidad

    def retornarvalores(self):
        for objeto in self.__listaCarrera:
            print(f'\t-Carrera: {objeto.getNombre()} Duracion: {objeto.getDuracion()}')
    
    def buscarigual(self,carrera):
        i:int = 0
        valor = None
        bandera = False
        valores = [None,None]
        while i < len(self.__listaCarrera) and bandera == False:
            if self.__listaCarrera[i].getNombre() == carrera:
                print('llegue')
                valores[0] = self.__listaCarrera[i].getCodigo()
                bandera = True
            i+=1
        valores[1] = bandera
        return valores

    def __str__(self):
        return ('Codigo: -{}- Facultad: -{}- Direccion: -{}- Localidad: -{}- Telefono: -{}-'.format(self.__codF,self.__nombreF,self.__direccion,self.__localidad,self.__telefono))
