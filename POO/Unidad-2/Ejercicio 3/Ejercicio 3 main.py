import csv
from Registro import Registro

def test():
    objeto = Registro(20.0,60,1009)
    print(objeto.muestra())

def iniciar(matrizz, listaA):
    for f in range(30):
        matrizz.append([])
        for c in range(24):
            matrizz[f].append(None)

    for linea in listaA:
        objeto = Registro(float(linea[2]), int(linea[3]), int(linea[4]))
        matriz[int(linea[0]) - 1][int(linea[1]) - 1] = objeto
    return matriz


def obtener(matrizz: list[list[Registro]], metodo: str) -> list[int, int, int, int]:
    menor = mayor = getattr(matrizz[0][0], metodo)()
    dmenor = dmayor = hmenor = hmayor = 0
    for i in range(30):
        for j in range(24):
            valor = getattr(matrizz[i][j], metodo)()
            if menor > valor:
                menor = valor
                dmenor = i
                hmenor = i
            if mayor < valor:
                mayor = valor
                dmayor = i
                hmayor = j
    return [dmayor, hmayor, dmenor, hmenor]


def maximominimo(matrizz: list[list[Registro]]):
    temperatura = obtener(matrizz, "getTemperatura")
    humedad = obtener(matrizz, "getHumedad")
    presion = obtener(matrizz, "getPresion")
    print(f'Temperatura Mayor: Dia: {temperatura[0] + 1} Hora: {temperatura[1] + 1} ')
    print(f'Temperatura Menor: Dia: {temperatura[2] + 1} Hora: {temperatura[3] + 1} ')
    print(f'Humedad Mayor: Dia: {humedad[0] + 1} Hora: {humedad[1] + 1} ')
    print(f'Humedad Menor: Dia: {humedad[2] + 1} Hora: {humedad[3] + 1} ')
    print(f'Presion Mayor: Dia: {presion[0] + 1} Hora: {presion[1] + 1} ')
    print(f'Presion Menor: Dia: {presion[2] + 1} Hora: {presion[3] + 1} ')


"""def mostrar(matriz):
    dias = 30
    horas = 24
    j = 0
    i = 0
    print('Hora: ', end="")
    for h in range(24):
        print('%10.d' % (j), end='')
        j += 1
    print('\n')
    for fila in range(dias):
        print(f'Dia: {i}', end="  ")
        for columna in range(horas):
            print(matriz[fila][columna], end='     ')
        print()
        i += 1"""


def promedio(matriz: list[list[Registro]]):
    promedioT: float = 0
    for j in range(24):
        acum: float = 0
        for i in range(30):
            acum += matriz[i][j].getTemperatura()
            promedioT = acum/30
        print('Hora: %d tiene un proemedio: %.2f' % (j+1, promedioT))


def listar(matriz: list[list[Registro]], dia):
    print('Hora\t\t\t Temperatura\t\t\t Hudedad\t\t\t Presion')
    for i in range(24):
        print("-%2d %20.2f %20d %20d" %(i+1, matriz[dia][i].getTemperatura(), matriz[dia][i].getHumedad(),matriz[dia][i].getPresion()))


if __name__ == '__main__':
    test()
    with open('Unidad-2-POO\Ejercicio 3\Registro.txt', 'r', encoding='utf8') as archivo:
        matriz = []
        reader = csv.reader(archivo, delimiter=',')
        matriz = iniciar(matriz, reader)
        # mostrar(matriz)

        opcion = None
        while opcion != 5:
            print('Menu Cuaderno'.center(30, '-'))
            print('1- Mostrar Minimo y Maximo')
            print('2- Promedio Temperatura por hora')
            print('3- Listar Variables de un dia')
            print('4- Salir')
            opcion = int(input('Tu opcion: '))
            if opcion == 1:
                print('\n')
                print('Variable Meterologicas'.center(30, '-'))
                maximominimo(matriz)
            elif opcion == 2:
                print('\n')
                print('Temperatura promedio por hora'.center(40, '-'))
                promedio(matriz)
            elif opcion == 3:
                print('\n')
                dia = int(input('Ingrese un dia:'))
                listar(matriz, dia-1)
            elif opcion == 4:
                print('Salimos del programa'.center(40, '-'))