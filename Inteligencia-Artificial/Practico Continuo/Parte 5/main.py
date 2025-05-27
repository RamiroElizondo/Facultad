import random

# Datos del problema
objetos = [(4,10), (2,4), (3,7), (1,1), (2,2), (5,8), (3,6)]
peso_max = 15
tamano_solucion = len(objetos)

# Función Objetivo
def evaluar(solucion):

    peso = sum(objetos[i][0] for i in range(len(solucion)) if solucion[i])
    valor = sum(objetos[i][1] for i in range(len(solucion)) if solucion[i])
    if peso > peso_max:
        return -1  # penalización si excede
    return valor


# Generar vecinos

def generar_vecinos(solucion):
    vecinos = []
    for i in range(tamano_solucion):
        vecino = solucion.copy()
        vecino[i] = 1 - vecino[i]
        vecinos.append(vecino)
    return vecinos


# Búsqueda Tabú
def tabu_search(iteraciones=20, tamano_tabu=5):
    # Inicialización
    solucion_actual = [random.randint(0,1) for _ in range(tamano_solucion)]
    mejor_solucion = solucion_actual[:]
    lista_tabu = []
    
    print("Población Inicial:")
    for _ in range(4):  # Mostrar 4 soluciones iniciales
        individuo = [random.randint(0,1) for _ in range(tamano_solucion)]
        print(individuo, "-> Valor:", evaluar(individuo))
    print("============")

    for iteracion in range(iteraciones):
        vecinos = generar_vecinos(solucion_actual)
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]
        vecinos_validos.sort(key=lambda x: evaluar(x), reverse=True)

        if not vecinos_validos:
            break

        mejor_vecino = vecinos_validos[0]
        solucion_actual = mejor_vecino[:]

        if evaluar(solucion_actual) > evaluar(mejor_solucion):
            mejor_solucion = solucion_actual[:]

        lista_tabu.append(solucion_actual)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)

        print(f"Iteración {iteracion + 1}:")
        print("Solución actual:", solucion_actual, "-> Valor:", evaluar(solucion_actual))
        print("Mejor hasta ahora:", mejor_solucion, "-> Valor:", evaluar(mejor_solucion))
        print("============")

    return mejor_solucion

# Ejecutar Búsqueda Tabú
mejor = tabu_search()
print(">> Mejor Solución Encontrada:", mejor, "-> Valor:", evaluar(mejor))
