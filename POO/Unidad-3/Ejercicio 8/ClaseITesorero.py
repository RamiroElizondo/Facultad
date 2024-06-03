from zope.interface import Interface

class ITesorero(Interface):#type: ignore
    def gastosSueldosporEmpleado(self,dni):
        pass
