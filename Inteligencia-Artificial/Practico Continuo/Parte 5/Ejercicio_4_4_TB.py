import numpy as np
import random
import time

class BusquedaTabuMochila:
    def __init__(self, pesos, valores, peso_maximo, duracion_tabu=5, max_iteraciones=100):
        self.pesos = pesos
        self.valores = valores
        self.peso_maximo = peso_maximo
        self.num_objetos = len(pesos)
        self.duracion_tabu = duracion_tabu
        self.max_iteraciones = max_iteraciones
        self.lista_tabu = {}  # Diccionario para almacenar movimientos tabú y su duración
        self.mejor_solucion = None
        self.mejor_valor = 0
    
    def evaluar_solucion(self, solucion):
        #Evaluar una solución, retornando el valor y si es factible
        peso_total = sum(self.pesos[i] for i in range(self.num_objetos) if solucion[i] == 1)
        valor_total = sum(self.valores[i] for i in range(self.num_objetos) if solucion[i] == 1)
        
        es_factible = peso_total <= self.peso_maximo
        
        if not es_factible:
            # Penalización para soluciones no factibles
            return -1
        
        return valor_total
    
    def generar_solucion_inicial(self):
        #Generar una solución inicial factible
        solucion = [0] * self.num_objetos
        
        # Ordenar objetos por relación valor/peso de forma descendente
        objetos = [(i, self.valores[i] / self.pesos[i]) for i in range(self.num_objetos)]
        objetos.sort(key=lambda x: x[1], reverse=True)
        
        peso_actual = 0
        for idx, _ in objetos:
            if peso_actual + self.pesos[idx] <= self.peso_maximo:
                solucion[idx] = 1
                peso_actual += self.pesos[idx]
        
        return solucion
    
    def obtener_vecindario(self, solucion):
        #Generar vecindario por cambio de un bit
        vecinos = []
        for i in range(self.num_objetos):
            vecino = solucion.copy()
            vecino[i] = 1 - vecino[i]  # Cambio 0->1 o 1->0
            vecinos.append((vecino, i))  # Guardar el vecino y el índice que se modificó
        return vecinos
    
    def es_tabu(self, indice_objeto, iteracion):
        #Verificar si un movimiento está en la lista tabú
        return indice_objeto in self.lista_tabu and iteracion < self.lista_tabu[indice_objeto]
    
    def resolver(self):
        #Ejecutar el algoritmo Búsqueda Tabú
        solucion_actual = self.generar_solucion_inicial()
        self.mejor_solucion = solucion_actual.copy()
        self.mejor_valor = self.evaluar_solucion(solucion_actual)
        
        iteracion = 0
        
        # Para visualización
        print("Iteración 0: Solución inicial =", solucion_actual, "Valor =", self.mejor_valor)
        
        while iteracion < self.max_iteraciones:
            iteracion += 1
            
            # Generar vecindario
            vecinos = self.obtener_vecindario(solucion_actual)
            
            # Evaluar vecinos
            mejor_vecino = None
            mejor_valor_vecino = -float('inf') # Representa el infinito negativo, que es un valor menor que cualquier otro número. Para asegurar que cualquier vecino válido será mejor.
            mejor_indice_movimiento = None
            
            for vecino, indice_movimiento in vecinos:
                valor_vecino = self.evaluar_solucion(vecino)
                # Si el movimiento no es tabú O si es mejor que la mejor solución conocida (criterio de aspiración)
                if (not self.es_tabu(indice_movimiento, iteracion) or valor_vecino > self.mejor_valor) and valor_vecino > mejor_valor_vecino:
                    mejor_vecino = vecino
                    mejor_valor_vecino = valor_vecino
                    mejor_indice_movimiento = indice_movimiento
            
            # Si no se encontró un vecino válido (puede ocurrir con penalizaciones)
            if mejor_vecino is None:
                # Intentar con solución aleatoria
                mejor_vecino = [random.randint(0, 1) for _ in range(self.num_objetos)]
                mejor_valor_vecino = self.evaluar_solucion(mejor_vecino)
                mejor_indice_movimiento = random.randint(0, self.num_objetos - 1)
            
            # Actualizar la solución actual
            solucion_actual = mejor_vecino
            
            # Actualizar la mejor solución si procede
            if mejor_valor_vecino > self.mejor_valor and mejor_valor_vecino >= 0:  # Solo si es factible
                self.mejor_solucion = mejor_vecino.copy()
                self.mejor_valor = mejor_valor_vecino
                print(f"Iteración {iteracion}: Nueva mejor solución encontrada = {self.mejor_solucion}, Valor = {self.mejor_valor}")
            
            # Actualizar la lista tabú
            self.lista_tabu[mejor_indice_movimiento] = iteracion + self.duracion_tabu
            
            # Mostrar progreso
            if iteracion % 10 == 0:
                print(f"Iteración {iteracion}: Mejor solución actual = {self.mejor_solucion}, Valor = {self.mejor_valor}")
        
        return self.mejor_solucion, self.mejor_valor
    
    def mostrar_resultados(self):
        #Mostrar resultados detallados de la solución
        if self.mejor_solucion is None:
            print("Todavía no se ha ejecutado el algoritmo.")
            return
        
        print("\n---- Resultados finales ----")
        print(f"Mejor solución: {self.mejor_solucion}")
        print(f"Valor total: {self.mejor_valor}")
        
        objetos_seleccionados = [i+1 for i in range(self.num_objetos) if self.mejor_solucion[i] == 1]
        peso_total = sum(self.pesos[i] for i in range(self.num_objetos) if self.mejor_solucion[i] == 1)
        
        print(f"Objetos seleccionados: {objetos_seleccionados}")
        print(f"Peso total: {peso_total}/{self.peso_maximo}")
        
        print("\nDetalle de objetos seleccionados:")
        print("Objeto | Peso | Valor")
        print("-"*20)
        for i in range(self.num_objetos):
            if self.mejor_solucion[i] == 1:
                print(f"{i+1:6d} | {self.pesos[i]:4d} | {self.valores[i]:5d}")


def main():
    # Permitir ingresar datos desde teclado
    usar_predeterminados = input("¿Usar datos predeterminados? (s/n): ").lower() == 's'
    
    if usar_predeterminados:
        pesos = [4, 2, 3, 1, 2, 5, 3]
        valores = [10, 4, 7, 1, 2, 8, 6]
        peso_maximo = 15
    else:
        num_objetos = int(input("Ingrese el número de objetos: "))
        pesos = []
        valores = []
        print("Ingrese pares (peso, valor) para cada objeto:")
        for i in range(num_objetos):
            p, v = map(int, input(f"Objeto {i+1} (peso valor): ").split())
            pesos.append(p)
            valores.append(v)
        
        peso_maximo = int(input("Ingrese el peso máximo de la mochila: "))
    
    # Configuración del algoritmo
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones (recomendado: 100): ") or "100")
    duracion_tabu = int(input("Ingrese el tamaño de la lista tabú (recomendado: 5): ") or "5")
    
    # Crear y ejecutar el algoritmo Búsqueda Tabú
    bt = BusquedaTabuMochila(pesos, valores, peso_maximo, duracion_tabu, max_iteraciones)
    
    tiempo_inicio = time.time()
    solucion, valor = bt.resolver()
    tiempo_fin = time.time()
    
    bt.mostrar_resultados()
    print(f"\nTiempo de ejecución: {tiempo_fin - tiempo_inicio:.4f} segundos")

    # Comparar con población inicial
    print("\n---- Visualización de una población inicial ----")
    tamaño_poblacion = 4
    print(f"Generando población inicial de {tamaño_poblacion} individuos:")
    
    poblacion = []
    valores_aptitud = []
    
    for i in range(tamaño_poblacion):
        # Generar un individuo aleatorio
        individuo = [random.randint(0, 1) for _ in range(len(pesos))]
        
        # Calcular la aptitud
        peso_total = sum(pesos[j] for j in range(len(pesos)) if individuo[j] == 1)
        if peso_total <= peso_maximo:
            aptitud = sum(valores[j] for j in range(len(valores)) if individuo[j] == 1)
        else:
            aptitud = 0  # Penalización para soluciones no factibles
        
        poblacion.append(individuo)
        valores_aptitud.append(aptitud)
        
        print(f"Individuo {i+1}: {individuo}, Aptitud: {aptitud}")

    print("\nMejor individuo en población inicial:")
    indice_mejor = valores_aptitud.index(max(valores_aptitud))
    print(f"Cromosoma: {poblacion[indice_mejor]}, Aptitud: {valores_aptitud[indice_mejor]}")
    print(f"\nComparación con solución final de Búsqueda Tabú:")
    print(f"Cromosoma: {solucion}, Aptitud: {valor}")


if __name__ == "__main__":
    main()