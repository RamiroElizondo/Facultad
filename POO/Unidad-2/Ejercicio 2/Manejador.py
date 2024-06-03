import csv
from ViajeroFrecuente import ViajeroFrecuente

posicion:int = 0
cont:int =0
class ManejadorViajero:
    __listaobjetos: list[ViajeroFrecuente]
    def __init__(self):
        self.__listaobjetos = []
    
    def test(self):
        objetoP = ViajeroFrecuente(250, 24941821, 'Ramiro', 'Elizondo', 1500)
        print('Prueba: {}'.format(objetoP.muestra()))
        print('Cantidad: {}'.format(objetoP.cantidadTotalMillas()))
        print('Acumula: {}'.format(objetoP.acumularMillas(1500)))
        print('Canjeo: {}'.format(objetoP.canjerarMillas(2000)))

    def cargarViajero(self):
        with open("Ejercicio 2\Datos.txt", 'r', encoding='utf8') as archivo:
            cont = 0
            reader = csv.reader(archivo, delimiter=',')
            for lineaA in reader:
                objeto = ViajeroFrecuente(int(lineaA[0]), (lineaA[1]), (lineaA[2]), lineaA[3], int(lineaA[4]))
                self.__listaobjetos.append(objeto)
                cont += 1

    def buscar(self):
        j:int = 0
        numero = int(input('Ingrese el numero de viajero frecuente: '))
        
        while j < len(self.__listaobjetos) and numero != self.__listaobjetos[j].getnumero():
            j+=1
        if j < len(self.__listaobjetos):
            posicion = j
            print(f'Encontrado: posicion: {posicion+1}'.center(30, '-'))
        else:
            print('No coinciden'.center(20, '-'))

    def consultarMillas(self):
        cant1 = self.__listaobjetos[posicion].cantidadTotalMillas()
        print('La cantidad total de millas acumuladas es {}\n'.format(cant1))

    def acumular(self):
        cant2 = int(input('Ingrese la cantidad de millas recorridas: '))
        valor1 = self.__listaobjetos[posicion].acumularMillas(cant2)
        print('Valor actualizado de las millas: {}\n'.format(valor1))
    
    def canjear(self):
        cant3 = int(input('Ingrese la cantidad de millas a canjear: '))
        valor2 = self.__listaobjetos[posicion].canjerarMillas(cant3)
        print('Valor de cantidad de millas acumuladas: {}\n'.format(valor2))