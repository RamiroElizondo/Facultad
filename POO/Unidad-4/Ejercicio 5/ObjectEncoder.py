import json
from ClasePaciente import Paciente

class ObjectEnconder:
    __lista: list[Paciente] = []
    __ruta:str

    def __init__(self):
        self.__ruta = "Ejercicio 5\\pacientes.json"
        self.cargarPacientes()
    
    def leerJson(self,archivo):
        with open(archivo, 'r',encoding='utf8') as f:
            pacientes = json.load(f)
        return pacientes
    
    def cargarPacientes(self):
        lista= []
        with open(self.__ruta,'r')as file:
            for data in json.load(file):
                objeto = Paciente(data['nombre'],data['apellido'],data['telefono'],data['altura'],data['peso'])
                lista.append(objeto)
        self.__lista =lista
    
    def getLista(self):
        return self.__lista

    def guarderJson(self):
        listaN = []
        for objeto in self.__lista:
            dicc = objeto.toJson()
            listaN.append(dicc)
        with open(self.__ruta, 'w',encoding='utf8') as f:
            json.dump(listaN,f,indent='\t')
    
    def getPaciente(self,indice):
        return self.__lista[indice]

    def addPaciente(self,paciente:Paciente):
        self.__lista.append(paciente)
        self.guarderJson()

    def renovar(self,pos,paciente:Paciente):
        self.__lista[pos] = paciente
        self.guarderJson()
    
    def borrar(self,pos):
        del self.__lista[pos]
        self.guarderJson()