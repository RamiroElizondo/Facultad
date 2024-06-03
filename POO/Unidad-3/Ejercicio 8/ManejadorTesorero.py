from zope.interface import implementer
from ClaseITesorero import ITesorero
from ClaseLista import ListaEnlazada


@implementer(ITesorero)
class ManejadorTesorero:
    __lista:ListaEnlazada

    def __init__(self,lista:ListaEnlazada):
        self.__lista = lista
        self.gastosSueldosporEmpleado(lista)
    
    def gastosSueldosporEmpleado(self,lista:ListaEnlazada):
        cuil = input('Ingrese el CUIL: ')
        bandera = False
        actual = lista.getComienzo()
        while actual != None and bandera == False:
            if actual.getDato().getCUIL()== cuil:
                print('El gasto de sueldo es: ',actual.getDato().getSueldoB()*actual.getDato().getAntiguedad())
                bandera = True
            actual = actual.getSiguiente()
        if bandera == False:
            print('El agente no existe')

