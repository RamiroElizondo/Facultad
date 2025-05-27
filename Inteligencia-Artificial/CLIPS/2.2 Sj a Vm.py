#Lista de adyacencia del grafo que muestra las conexiones entre los nodos
grafo = {
    1: [2],
    2: [1, 3, 4],
    3: [2, 5],
    4: [2, 8, 9],
    5: [3, 6, 7],
    6: [5, 7, 18],
    7: [5, 6, 8],
    8: [4, 7, 10, 12, 13],
    9: [4, 10, 11],
    10: [8, 9, 11],
    11: [9, 10, 12, 14],
    12: [8, 11, 13, 15],
    13: [8, 12, 16, 18],
    14: [11, 15],
    15: [12, 14, 16],
    16: [13, 15, 17],
    17: [16, 18],
    18: [6, 13, 17],
}

# Función para encontrar todos los caminos posibles
def encontrar_caminos(grafo, inicio, fin, camino=[]):
    camino = camino + [inicio]
    if inicio == fin:
        return [camino]
    caminos = []
    for nodo in grafo[inicio]:
        if nodo not in camino:
            nuevos_caminos = encontrar_caminos(grafo, nodo, fin, camino)
            for nuevo_camino in nuevos_caminos:
                caminos.append(nuevo_camino)
    return caminos

# Buscamos todos los caminos de 1 a 18
todos_los_caminos = encontrar_caminos(grafo, 1, 18)

# Imprimimos los caminos
for camino in todos_los_caminos:
    print(camino)

print(f"\nTotal de caminos encontrados: {len(todos_los_caminos)}")