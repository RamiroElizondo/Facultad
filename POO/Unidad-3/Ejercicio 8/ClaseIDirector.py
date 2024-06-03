from zope.interface import Interface

class IDirector(Interface):#type: ignore
    def modificarBasico(self,dni,nuevoB):
        pass

    def modificarPorcentajeporCargo(self,dni,nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoria(self,dni,nuevoporcentaje):
        pass

    def modificarImporteExtra(self,dni,nuevoImporteExtra):
        pass