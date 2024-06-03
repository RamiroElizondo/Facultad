import os
from Menu import Menu
from Manejador import ManejadorPlan
import os


if __name__ == '__main__':
    os.system("cls")
    maP = ManejadorPlan()
    maP.test()
    maP.cargarObjetos()
    opcion = None
    menu = Menu()
    while opcion != 5:
        menu.mostrar()
        opcion = int(input('Tu ocpion: '))
        menu.menuopciones(opcion)
    else:
            print('Saliendo del Programa'.center(30,'-'))