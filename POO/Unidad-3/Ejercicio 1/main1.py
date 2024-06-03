from Menu import Menu


if __name__ == '__main__':
    menu = Menu()
    opcion = None
    while opcion != 0:
        menu.mostrar()
        opcion = int(input('Su opcion: '))
        menu.menuopciones(opcion)
    else: 
        print('Salio del Programa')