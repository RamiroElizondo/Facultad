from Conjunto import Conjunto
from Menu import Menu

if __name__ == "__main__":
    menu = Menu()
    opcion = None
    while opcion != 4:
        menu.mostrar()
        opcion = int(input('Tu opcion: '))
        menu.menuopciones(opcion)
    else:
        print('Saliendo del Menu')