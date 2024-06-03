import csv
from ViajeroFrecuente import ViajeroFrecuente

def buscar(listaobjetos):
    i = 0
    bandera = False
    while bandera == False and i < len(listaObjetos):
        if listaObjetos[i].getNumero() == numero:
            bandera = True
            objeto = listaObjetos[i]
            print('Viajero Encontrado')
        i += 1
    if i > len(listaObjetos):
        print('Se sobre paso el limite')
        raise Exception()
    return objeto

if '__main__' == __name__:
    with open('Ejercicio 2\datos.csv','r',encoding='utf8')as archivo:
        reader = csv.reader(archivo,delimiter=',')
        listaObjetos = []

        for linea in reader:
            objeto = ViajeroFrecuente(int(linea[0]),linea[1],linea[2],linea[3],int(linea[4]))
            listaObjetos.append(objeto)
        
        #print(objeto.Mostrar())
        opcion = None
        while opcion != 'g':
            print('d- Determinar viajero con mayor cantidad de millas acumuladas')
            print('e- Acumular Millas Sobrecargar')
            print('f- Canjear Millas Sobrecarga')
            opcion = input('Tu opcion ')

            
            if opcion == 'd':
                maximo = listaObjetos[0]
                for objeto in listaObjetos:
                    if objeto > maximo:
                        maximo = objeto
                print('El viajero -{}- tiene la mayor cantidad de millas acumuladas'.format(maximo.getNombre()))
            elif opcion == 'e':
                numero = int(input('Ingrese un numero de Viajero Frecuente: '))
                objeto = buscar(objeto)
                millas = int(input('Ingrese millas acumular: '))
                objeto = objeto + millas
                print('Sus millas actualmente son -{}-'.format(objeto.cantidadTotalMillas()))
            elif opcion == 'f':
                numero = int(input('Ingrese un numero de Viajero Frecuente: '))
                objeto = buscar(objeto)
                millas = int(input('Ingrese millas a canjear: '))
                objeto = objeto - millas
                print('Sus millas actualmente son -{}-'.format(objeto.cantidadTotalMillas()))
            else:
                print('Accion no valida')