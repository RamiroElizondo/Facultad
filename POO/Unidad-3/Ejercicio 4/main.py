"""
Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo.
"""
from ManejadorCalefactor import ManejadorCalefactor


if __name__ == "__main__":
    archivo1 = open("calefactor-a-gas-1.csv",'r')
    archivo2 = open("calfactor-electrico-1.csv",'r')
    manC = ManejadorCalefactor()
    tamaño = int(input("Ingrese el tamaño del arreglo: "))
    manC.Cargar(archivo1,archivo2,tamaño)
    archivo1.close()
    archivo2.close()
    opcion = None
    indice1 = 0
    indice2 = 0
    while opcion != 0:
        print('Menu Opciones'.center(30,'-'))
        print('0- Salir')
        print('1- Menor Consumo Gas')
        print('2- Menor Consumo Electrico')
        print('3- Mostrar todos los datos del calefactor de menor consumo')
        opcion = int(input('Tu opcion:'))
        if opcion == 1:
            indice1 = print(manC.MenorConsumoGas())
        elif opcion == 2:
            indice2 = print(manC.MenorConsumoElectrico())
        elif opcion == 3:
            manC.Mostrar(indice1,indice2)
        elif opcion != 0 and opcion != 1 and opcion != 2 and opcion != 3:
            print('Opcion no valida')
    else:
        print('Fin del programa')