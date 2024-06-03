import csv
from Registro import Registro


def definir():
    lista = []
    for dia in range(30):
        lista.append([])
        for hora in range(24):
            lista[dia].append('-')
    return lista

def cargar(lista: list[list[Registro]],reader):
    for linea in reader:
        objeto = Registro(float(linea[2]),int(linea[3]),int(linea[4]))
        lista[int(linea[0])-1][int(linea[1])-1] = objeto

def mostrar(lista,dia):
    print('Hora \t Tempertatura \tHumudad \tPresion ')
    for hora in range(24):
        print(' %d \t     %.2f \t  %d \t\t %d' %(hora+1,lista[dia][hora].getTemperatura(),lista[dia][hora].getHumedad(),lista[dia][hora].getPresion()))

def maximoMinimo(lista: list[list[Registro]],metodo):
    maximo = getattr(lista[0][0],metodo)()
    diaM = horaM = 0
    for dia in range(30):
        for hora in range(24):
            valor = getattr(lista[dia][hora],metodo)()
            if maximo < valor:
                maximo = valor
                diaM =  dia
                horaM = hora
    print('Valor Maximo: {} Dia -{}- Hora -{}- '.format(maximo,diaM+1,horaM+1))
    diaM = horaM = 0
    minimo = getattr(lista[0][0],metodo)()
    for dia in range(30):
        for hora in range(24):
            valor = getattr(lista[dia][hora],metodo)()
            if minimo > valor:
                minimo = valor
                diaM =  dia
                horaM = hora
    print('Valor Minimo: {} Dia -{}- Hora -{}- \n'.format(minimo,diaM+1,horaM+1))

def promedio(lista):
    for hora in range(24):
        promedio = 0
        acum = 0
        print('Hora: {}'.format(hora+1),end='   ')
        for dia in range(30):
            acum += lista[dia][hora].getTemperatura()
        promedio = acum / 24
        print('Promedio: %.2f'%(promedio))


if '__main__' == __name__:
    with open('Ejercicio 3\Datos.csv','r',encoding='utf8') as archivo:
        reader = csv.reader(archivo,delimiter=',')
        lista = definir()
        cargar(lista,reader)
        #mostrar(lista,5)

        opcion = None

        while opcion != 4:
            print('Menu de Opciones')
            print('1- Menor y Mayor valor de cada variables')
            print('2- Temperatura promedio mensual por hora')
            print('3- Dado un dia listar valores')
            opcion =int(input('Tu opcion: '))

            if opcion == 1:
                print('Temperatura')
                maximoMinimo(lista,'getTemperatura')
                print('Humedad')
                maximoMinimo(lista,'getHumedad')
                print('Presion')
                maximoMinimo(lista,'getPresion')
            elif opcion == 2:
                promedio(lista)
            elif opcion == 3:
                dia = int(input('Ingrese dia: '))
                mostrar(lista,dia)
