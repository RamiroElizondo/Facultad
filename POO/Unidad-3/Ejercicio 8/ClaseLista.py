from zope.interface import implementer
from ClaseInterfaz import Interfaz
from ClaseNodo import Nodo
from ClaseDocente import Docente
from ClaseInvestigador import Investigacion
from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePersonalApoyo import PersonalApoyo

@implementer(Interfaz)
class ListaEnlazada:
    __comienzo: Nodo | None
    
    def __init__(self):
        self.__comienzo = None

    def agregar(self,objeto):
        nodo = Nodo(objeto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def getTamaño(self)->int:
        contador:int = 0
        actual = self.__comienzo
        while actual != None:
            contador += 1
            actual = actual.getSiguiente()
        return contador

    def insertarElemento(self,objeto,pos:int):
        pos = pos -1
        if pos > self.getTamaño()-1:
            raise Exception("Fuera de Rango")
        actual = self.__comienzo
        previo = None
        indice = 0 
        if pos == 0:
            self.agregar(objeto)
        else:
            nuevoNodo = Nodo(objeto)
            while indice < pos:
                indice +=1
                previo = actual
                actual = actual.getSiguiente()#type:ignore
            previo.setSiguiente(nuevoNodo)#type:ignore
            nuevoNodo.setSiguiente(actual)

    def agregarElemento(self,objeto):
        actual = self.__comienzo
        previo = None
        pos = 0
        tamaño = self.getTamaño()
        while pos < tamaño:
            previo = actual
            actual = actual.getSiguiente()#type:ignore
            pos += 1
        nuevoNodo = Nodo(objeto)
        if previo is None:
            nuevoNodo.setSiguiente(actual)
            self.__comienzo = nuevoNodo
        else:
            previo.setSiguiente(nuevoNodo)

    def mostrarLista(self):
        actual = self.__comienzo
        while actual is not None:
            print(actual.getDato())
            actual = actual.getSiguiente()

    def mostrarElemento(self,pos):
        pos = pos -1
        actual = self.__comienzo
        indice = 0
        bandera = False
        while actual != None and bandera == False:
            if indice == pos:
                print('Elemento Encontrado')
                tipo = type(actual.getDato())
                print(tipo)
                if tipo == Docente:
                    print('El agente es tipo Docente')
                elif tipo == Investigacion:
                    print('El agente es tipo Investigacion')
                elif tipo == DocenteInvestigador:
                    print('El agente es tipo DocenteInvestigador')
                elif tipo == PersonalApoyo:
                    print('El agente es tipo PersonalApoyo')
                bandera = True
            indice += 1
            actual = actual.getSiguiente()
        if indice > self.getTamaño():
            print('Elemento no Encontrado')

    def __iter__(self):
        actual = self.__comienzo
        while actual != None:
            yield actual.getDato()
            actual = actual.getSiguiente()

    def getComienzo(self):
        return self.__comienzo