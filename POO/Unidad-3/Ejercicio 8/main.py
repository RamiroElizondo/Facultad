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
DocenteInvestigador
2192921
Elizondo
Ramiro
200112
4
LSI
Simple
hola
Computacional
Cientifico
III
9022
2
DocenteInvestigador
29212321
Perez
Juan
291212
5
LCC
Semiexclusivo
hola2
Electronica
Cuantica
III 
21221
"""