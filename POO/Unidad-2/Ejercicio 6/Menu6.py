from Manejador6 import ManejadorViajero


class Menu:
    __instancia = ManejadorViajero

    def __init__(self):
        self.__instancia = ManejadorViajero()

    def mostrar(self):
        print('Menu Cuaderno'.center(30, '-'))
        print('a- Consultar Cantidad de Millas')
        print('b- Acumular Millas')
        print('c- Canjear Millas')
        print('d- Salir')

    def opcion1(self):
        self.__instancia.consultarMillas()

    def opcion2(self):
        self.__instancia.acumular()

    def opcion3(self):
        self.__instancia.canjear()

    def menuopciones(self, opcion):
        if opcion == 'a':
            self.opcion1()
        elif opcion == 'b':
            self.opcion2()
        elif opcion == 'c':
            self.opcion3()
        elif opcion != 'a' and opcion != 'b' and opcion != 'c':
            print('Opcion no valida'.center(30, '-'))
