from zope.interface import implementer
from ClaseIDirector import IDirector
from ClaseLista import ListaEnlazada
from ClaseDocente import Docente
from ClaseInvestigador import Investigacion
from ClaseDocenteInvestigador import DocenteInvestigador

@implementer(IDirector)
class ManejadorDirector:
    __lista: ListaEnlazada

    def __init__(self, lista:ListaEnlazada):
        self.__lista = lista
        self.menu()
    
    def menu(self):
        opcion = None
        while opcion != 0:
            print('Menu Opciones'.center(30,'-'))
            print('0- Salir')
            print('1- Modificar Basico')
            print('2- Modificar Porcentaje por Cargo')
            print('3- Modificar Porcentaje por Categoria')
            print('4- Modificar Importe Extra')
            opcion = int(input('Tu opcion: '))
            if opcion == 1:
                cuil = input('Ingrese el cuil del director: ')
                nuevoB = float(input('Ingrese el nuevo basico: '))
                self.modificarBasico(cuil,nuevoB)
            elif opcion == 2:
                cuil = input('Ingrese el cuil del director: ')
                nuevoPorcentaje = float(input('Ingrese el nuevo porcentaje: '))
                self.modificarPorcentajeporCargo(cuil,nuevoPorcentaje)
            elif opcion == 3:
                cuil = input('Ingrese el cuil del director: ')
                nuevoPorcentaje = float(input('Ingrese el nuevo porcentaje: '))
                self.modificarPorcentajeporcategoria(cuil,nuevoPorcentaje)
            elif opcion == 4:
                cuil = input('Ingrese el cuil del director: ')
                nuevoImporteExtra = float(input('Ingrese el nuevo importe extra: '))
                self.modificarImporteExtra(cuil,nuevoImporteExtra)
    
    def modificarBasico(self,cuil,nuevoB):
        actual = self.__lista.getComienzo()
        bandera = False
        cate = input('Ingrese la categoria: ')
        while actual != None and bandera == False:
            if actual.getDato().getCUIL() == cuil:
                actual.getDato().setBasico(nuevoB)
                print('Sueldo Modificado')
                bandera = True
            actual = actual.getSiguiente()

    def modificarPorcentajeporCargo(self,cuil,nuevoPorcentaje):
        cargo = input('Ingrese el cargo: ')
        bandera = False
        actual = self.__lista.getComienzo()
        while actual != None and bandera == False:
            if actual.getDato().getCUIL() == cuil and isinstance(actual.getDato(),Docente):
                actual.getDato().setPorcentajeCargo(cargo,nuevoPorcentaje)
                print('Porcentaje Modificado')
                bandera = True
            actual = actual.getSiguiente()

    def modificarPorcentajeporcategoria(self,cuil,nuevoporcentaje):
        cate = input('Ingrese el categoria: ')
        bandera = False
        actual = self.__lista.getComienzo()
        while actual != None and bandera == False:
            if actual.getDato().getCUIL() == cuil and isinstance(actual.getDato(),Investigacion):
                actual.getDato().setPorcentajeCategoria(cate,nuevoporcentaje)
                print('Porcentaje Modificado')
                bandera = True
            actual = actual.getSiguiente()

    def modificarImporteExtra(self,cuil,nuevoImporteExtra):
        bandera = False
        actual = self.__lista.getComienzo()
        while actual != None and bandera == False:
            if actual.getDato().getCUIL() == cuil and isinstance(actual.getDato(),DocenteInvestigador):
                actual.getDato().setExtra(nuevoImporteExtra)
                print('Importe Extra Modificado')
                bandera = True
            actual = actual.getSiguiente()