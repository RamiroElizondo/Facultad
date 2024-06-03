import os
from Menu import Menu
from Manejador import ManejadorViajero




if __name__ == "__main__":
    os.system("cls")
    manViajero = ManejadorViajero()
    manViajero .test()
    manViajero.cargarViajero()
    manViajero.buscar()
    menu = Menu()
    opcion = None
    while opcion != 'd':
        menu.mostrar()
        opcion = input('Tu opcion: ')
        menu.menuopciones(opcion)
    else:
        print('Salimos del programa'.center(30, '-'))
