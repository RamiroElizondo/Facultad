from ManejadoJugador import ManejadaorJugador
from ManejadorContratos import ManejadorContratos
from ManejadorEquipo import ManejadorEquipos


class Menu:
    __equipo: ManejadorEquipos
    __jugador: ManejadaorJugador
    __contrato: ManejadorContratos

    def __init__(self):
        self.__equipo = ManejadorEquipos()
        self.__jugador = ManejadaorJugador()
        self.__contrato = ManejadorContratos()
        self.__equipo.cargarEquipo()
        self.__jugador.cargarJugador()
        
    
    def mostrar(self):
        print('Menu Opciones'.center(30,'-'))
        print('0- Salir')
        print('1- Hacer Contrato')
        print('2- Consultar Jugador Contrado')
        print('3- Consultar Contratos')
        print('4- Obtener Import de Contratos')
        print('5- Guardar Contratos')
    
    def opcion1(self):
        self.__contrato.hacercontrato(self.__jugador,self.__equipo)

    def opcion2(self):
        dni = input('Ingrese DNI: ')
        self.__contrato.buscarJugador(dni)

    def opcion3(self):
        nombre = input('Ingrese Nombre de un Equipo: ')
        self.__contrato.consultarContrato(nombre,self.__equipo)

    def opcion4(self):
        nombre = input('Ingrese Nombre de un Equipo: ')
        self.__contrato.obtenerImporte(nombre,self.__equipo)

    def opcion5(self):
        self.__contrato.guardarContratos()

    def menuOp(self,opcion):
        if opcion == 1:
            self.opcion1()
        elif opcion == 2:
            self.opcion2()
        elif opcion == 3:
            self.opcion3()
        elif opcion == 4:
            self.opcion4()
        elif opcion == 5:
            self.opcion5()
        elif opcion != 0 and opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
            print('Opcion no valida')
