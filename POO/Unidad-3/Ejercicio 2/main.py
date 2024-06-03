from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos


if __name__ == '__main__':
    manF = ManejadorFlores()
    manR = ManejadorRamos()
    arreglo = manF.cargaFlores()
    
    opcion = None
    while opcion != 4:
        print('Menu Opciones'.center(30,'-'))
        print('1- Registrar Ramo')
        print('2- Mostrar las 5 floreas mas pedidas')
        print('3- Mostrar flores vendidad en un Tipo de Ramo')
        print('4- Salir')
        opcion = int(input('Tu ocpion: '))
        if opcion == 1:
            tamaño = input('Tamaño? Chico = 1 Mediano = 2 Grande = 4: ')
            valor = manR.AsignarT(tamaño)
            manR.cargarRamos(int(valor),tamaño)

        elif opcion == 2:
            manR.maspedidas(arreglo)

        elif opcion == 3:
            tipo = input('Ingrese un tipo de ramo: ')
            manR.mostrarTipo(tipo)

        elif opcion != 1 or opcion != 2 or opcion != 3:
            print('Opcion Incorrecta')
    else:
        print('Saliendo del programa'.center(30,'-'))

#Lote de prueba
"""
1
Mediano
Nomeolvides
Cactus de navidad
1
Grande
Nomeolvides
Nomeolvides
Girasoles
Girasoles
1
Grande
Boca de dragon
Boca de dragon
Boca de dragon
Boca de dragon
1
Grande
Cactus de navidad
Cactus de navidad
Cactus de navidad
Cactus de navidad
1
Chico
Ave del paraiso


"""