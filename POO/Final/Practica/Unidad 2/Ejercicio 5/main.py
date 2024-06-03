import csv
from PlanAhorro import PlanAhorro


def actualizar(lista):
    for objeto in lista:
        print('Plan: -{}- Modelo: -{}- Version: -{}- Valor Actual: -{}-'.format(objeto.getcodPlan(),objeto.getModelo(),objeto.getVersion(),objeto.getValor()))
        valor = int(input('Ingrese el valor actual de vehiculo: '))
        objeto.setValor(valor)
def calcular(objeto):
    valorCuota = (objeto.getValor()/objeto.getcantCuotasP()) * + objeto.getValor() * 0.10

    return valorCuota

def mostrar(lista):
    valor = int(input('Ingrese un valor de cuota'))
    i = 0
    bandera = False
    while bandera == False and i <= len(lista):
        if calcular(lista[i]) < valor:
            print('Plan {} con valor de cuota inferior al ingresado'.format(lista[i].getcodPlan()))
            print('Modelo: {} Version: {}'.format(lista[i].getModelo(),lista[i].getVersion()))

def mostrarMonto(lista):
    for objeto in lista:
        print('En el plan: {}'.format(objeto.getcodPlan()))
        print('Se debe haber pagado: {}'.format(calcular(objeto)*objeto.setcantidadCuotasPagar(valor)))

if '__main__' == __name__:
    with open('Ejercicio 5\planes.csv','r',encoding='utf8')as archivo:
        reader = csv.reader(archivo,delimiter=';')
        lista = []
        for linea in reader:
            objeto = PlanAhorro(int(linea[0]),linea[1],linea[2],int(linea[3]))
            PlanAhorro.setcantidadCuotasP(int(linea[4]))
            PlanAhorro.setcantidadCuotasPagar(int(linea[5]))
            lista.append(objeto)
        
        opcion = None
        while opcion != 'e':
            print('Menu de Opciones')
            print('a- Actualizar valor de vehiculo')
            print('b- Mostrar en base a un calr de cuota menor')
            print('c- Mostrar monto que se debe haber pagado para licitar el vehiculo')
            print('d- Modificar cantidad de cuotas a licitar')
            opcion = input('Tu Opcion: ')

            if opcion == 'a':
                actualizar(lista)
            elif opcion == 'b':
                mostrar(lista)
            elif opcion == 'c':
                mostrarMonto(lista)
            elif opcion == 'd':
                valor = int(input('Ingrese la nueva cantidad de cuotas apra licitar: '))
                PlanAhorro.setcantidadCuotasPagar(valor)