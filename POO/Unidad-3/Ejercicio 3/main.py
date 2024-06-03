from Menu import Menu


if __name__ == '__main__':
    menu = Menu()
    opcion = None
    while opcion != 0:
        menu.mostrar()
        opcion = int(input('Tu opcion: '))
        menu.menuOp(opcion)
    else: 
        print('Saliendo del Programa')

#Lote de proebas
"""
1
si
River
228193
2/11/2018
1/11/2025
Si
River
312122
22/10/2024
12/12/2026
si
Racing Club
172234
8/6/2019
3/11/2024
no
si
San Lorenzo
250946
19/1/2019
12/11/2022
si
San Martin
231185
29/6/2018
10/11/2024
si
Boca
296631
11/2/2018
25/7/2024
no
no
no
no
"""