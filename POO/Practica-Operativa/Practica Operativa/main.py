#Tema 1
from ManejadorPersonal import ManejadorPersonal
from ManejadorNovedades import ManejadorNovedades

if __name__ == '__main__':
    manP = ManejadorPersonal()
    manN = ManejadorNovedades()
    manP.cargarArreglo()
    manN.cargarNovedades(manP)
    manP.calcularSueldos(manN)
    opcion = None
    while opcion != 'd':
        print('Menu Opciones'.center(30,'-'))
        print('a- Obtener sueldo a Liquidar segun legajo')
        print('b- Obtener Listado')
        print('c- Obtener sueldo a cobrar mas bajo')
        opcion = input('Tu Opcion: ')
        if opcion == 'a':
            numero = int(input('Ingrese Un legajo: '))
            manP.buscaLegajo(numero,manN)

        elif opcion == 'b':
            manP.listado(manN)

        elif opcion == 'c':
            manP.buscarMenor()
    else:
        print('Saliendo del programa')
