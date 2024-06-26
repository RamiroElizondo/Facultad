"""
Ejercicio 1
Definir el T.A.D Grafo/Digrafo:
a) Especificación.
b) Representación (para la representación secuencial de grafo, utilizar arreglo unidimensional)
c) Implementación de todas las operaciones.
"""
from cola import Cola
from pila import Pila
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo = nodo
        self.conocido = conocido
        self.distancia = distancia
        self.camino = camino

class Grafo:
    __matrizA: np.ndarray

    def __init__(self,aristas):
        self.__matrizA = np.full((6,6),0)
        self.__pesos = np.full((6,6),1)
        for arista in aristas:
            self.__matrizA[arista[0]][arista[1]] = 1
            self.__matrizA[arista[1]][arista[0]] = 1

    def getPeso(self,vertice1,vertice2):
        return self.__pesos[vertice1][vertice2]

    def mostrar(self):
        for i in range(6):
            for j in range(6):
                print(self.__matrizA[i][j],end=' ')
            print('\n')

    def adyacentes(self,vertice):
        arreglo= []
        for i in range(len(self.__matrizA)):
            if self.__matrizA[vertice][i] == 1:
                arreglo.append(i)
        return arreglo

    def REA(self, vertice):
        print('Recorrido en anchura: ',vertice)
        visitado = []
        cola = Cola()
        cola.insertar(vertice)
        while cola.getTamaño() > 0:
            actual = cola.suprimir().getValor()
            if actual not in visitado:
                visitado.append(actual)  # Marcar el vértice como visitado
                ady = self.adyacentes(actual)
                # Agregar los vecinos no visitados del vértice actual a la cola
                for w in ady:
                    cola.insertar(w)
        return visitado

    def REP(self,vertice):
        visitado = []
        pila = Pila()
        pila.insertar(vertice)
        while pila.getTamaño() > 0:
            actual = pila.suprimir()
            if actual not in visitado:
                visitado.append(actual)
                ady = self.adyacentes(actual)
                for w in ady:
                    pila.insertar(w)
        return visitado

    def camino(self, vertice1, vertice2):
        camino = []
        pila = Pila()
        pila.insertar(vertice1)
        while pila.getTamaño() > 0:
            v = pila.suprimir()
            if v not in camino:
                camino.append(v)
                if v == vertice2:
                    return camino
                ady = self.adyacentes(v)
                for w in ady:
                    pila.insertar(w)
        return camino

    def Aciclico(self):
        visitados = []
        pila = Pila()
        pila.insertar(0)
        while pila.getTamaño() > 0:
            v = pila.suprimir()
            if v not in visitados:
                visitados.append(v)
                ady = self.adyacentes(v)
                for w in ady:
                    if w in visitados:
                        return False
                    pila.insertar(w)
        return True

    def esConexo(self,vertices):
        visitados = self.REP(vertices[0])
        return len(visitados) == len(vertices)

    def caminoMinimo(self,verticeOrigen,verticeDestino,vertices):
        camino = self.dijkstra(verticeOrigen,vertices)
        if camino[verticeDestino] == None:
            return 'No hay camino'
        else:
            v = verticeDestino
            caminoMinimo = []
            while v != None:
                caminoMinimo.append(v)
                v = camino[v].camino
            caminoMinimo.reverse()
            return caminoMinimo

    def dijkstra(self,verticeOrigen,vertices):
        Tabla = {}
        for vertice in vertices:
            Tabla[vertice] = Registro(vertice,False,999999999,None)
        Tabla[verticeOrigen].distancia = 0
        
        for i in range(len(vertices)):
            #Buscar el vertice con menor distancia y que no haya sido visitado
            v = None
            for vertice in vertices:
                if not Tabla[vertice].conocido:
                    if v == None or Tabla[vertice].distancia < Tabla[v].distancia:
                        v = vertice
            Tabla[v].conocido = True
            #Actualizar los registros de los adyacentes
            for w in self.adyacentes(v):
                if Tabla[v].distancia + self.getPeso(v,w) < Tabla[w].distancia:
                    Tabla[w].distancia = Tabla[v].distancia + self.getPeso(v,w)
                    Tabla[w].camino = v
        return Tabla

    def grafico(self,vertices, adyacencia):
        G = nx.Graph()
        G.add_nodes_from(vertices)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()
if __name__ == '__main__':
    vertices = [0,1,2,3,4,5]
    aristas = [[0,1],[2,5],[2,3],[3,4],[4,5],[1,2]]
    grafo = Grafo(aristas)
    grafo.mostrar()

    vertice = int(input('Ingrese un Vertice: '))
    if vertice in vertices:
        print('Los vertices adyacentes a',vertice,'son: ')
        print(grafo.adyacentes(vertice))
        print('Recorrido en anchura: ',grafo.REA(vertice))
        print('Recorrido en profundidad: ',grafo.REP(vertice))

    print('El camino entre 0 y 5 es: ',grafo.camino(0,5))
    # Salida: El camino más corto entre 0 y 5 es:  [0, 1, 2, 3, 5]

    print('Es conexo? ',grafo.esConexo(vertices))
    print('Es asiclico? ',grafo.Aciclico())
    print('El camino minimo entre 0 y 5: ',grafo.caminoMinimo(0,5,vertices))


    grafo.grafico(vertices,aristas)
