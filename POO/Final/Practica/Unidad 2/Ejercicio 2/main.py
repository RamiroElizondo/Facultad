import csv
from ViajeroFrecuente import ViajeroFrecuente


if '__main__' == __name__:
    with open('Ejercicio 2\datos.csv','r',encoding='utf8')as archivo:
        reader = csv.reader(archivo,delimiter=',')
        listaObjetos = []

        for linea in reader:
            objeto = ViajeroFrecuente(int(linea[0]),linea[1],linea[2],linea[3],int(linea[4]))
            listaObjetos.append(objeto)
        
        numero = int(input('Ingrese un numero de Viajero Frecuente: '))
        
        i = 0
        bandera = False
        while bandera == False and i < len(listaObjetos):
            if listaObjetos[i].getNumero() == numero:
                bandera = True
                objeto = listaObjetos[i]
                print('Viajero Encontrado')
            i += 1
        if i >= len(listaObjetos):
            print('Se sobre paso el limite')
            raise Exception()
        #print(objeto.Mostrar())
        opcion = None
        while opcion != 'd':
            print('a- Consultar cantidad de millas')
            print('b- Acumular Millas')
            print('c- Canjear Millas')
            opcion = input('Tu opcion ')

            if opcion == 'a':
                print('Sus millas acumuladas son: {}'.format(objeto.cantidadTotalMillas()))
            elif opcion == 'b':
                cantidad = int(input('Ingrese la cantidad de millas a acumular: '))
                print('Sus millas son: {}'.format(objeto.acumularMillas(cantidad)))
            elif opcion == 'c':
                millas = int(input('Ingrese la cantidad de millas que desea canjear: '))
                print('Millas restantes: {}'.format(objeto.canjearMillas(millas)))
            else:
                print('Accion no valida')