from Menu import Menu


if __name__ == '__main__':
    menu = Menu()
    opcion = None
    while opcion != 0:
        menu.mostrar()
        opcion = int(input('Tu Opcion: '))
        menu.menuOpciones(opcion)
    else:
        print('Fin del Programa')

"""
1
1
Televisor
Philips
grande
gris
Chile
201212
2120x2921
Si
HD
No
2
Lavarropa
Liliana
chica
blanca
Peru
201213
5
2
Superior
1
4
2
Heladera
Philips
larga
Azul
España
23921
34
Si
No
4
5
6
7
"""