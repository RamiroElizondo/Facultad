import random
import time
import matplotlib.pyplot as plt

class AlgoritmoGeneticoMochila:
    def __init__(self, pesos, valores, peso_maximo, tam_poblacion=50, prob_cruce=0.8, 
                 prob_mutacion=0.1, num_generaciones=100, metodo_aptitud="valor", factor_cantidad=0.2):
        self.pesos = pesos
        self.valores = valores
        self.peso_maximo = peso_maximo
        self.num_objetos = len(pesos)
        self.tam_poblacion = tam_poblacion
        self.prob_cruce = prob_cruce
        self.prob_mutacion = prob_mutacion
        self.num_generaciones = num_generaciones
        self.metodo_aptitud = metodo_aptitud
        self.factor_cantidad = factor_cantidad
        
        self.mejor_individuo = None
        self.mejor_aptitud = 0
        self.historico_aptitud = []
        
        if metodo_aptitud == "valor_cantidad":
            self.valor_promedio = sum(valores) / len(valores)
        
        print(f"Método de aptitud: {metodo_aptitud}")
    
    def generar_poblacion_inicial(self):
        """Genera población inicial con mayor diversidad"""
        poblacion = []
        
        # 20% completamente aleatorio
        for _ in range(int(self.tam_poblacion * 0.2)):
            individuo = [random.randint(0, 1) for _ in range(self.num_objetos)]
            poblacion.append(individuo)
        
        # 30% basado en ratio valor/peso (greedy)
        ratios = [(self.valores[i]/self.pesos[i], i) for i in range(self.num_objetos)]
        ratios.sort(reverse=True)
        
        for _ in range(int(self.tam_poblacion * 0.3)):
            individuo = [0] * self.num_objetos
            peso_actual = 0
            indices_mezclados = [idx for _, idx in ratios]
            random.shuffle(indices_mezclados)  # Añadir aleatoriedad
            
            for idx in indices_mezclados:
                if peso_actual + self.pesos[idx] <= self.peso_maximo:
                    if random.random() < 0.8:  # 80% probabilidad de tomar objeto bueno
                        individuo[idx] = 1
                        peso_actual += self.pesos[idx]
            poblacion.append(individuo)
        
        # 50% restante completamente aleatorio
        while len(poblacion) < self.tam_poblacion:
            individuo = [random.randint(0, 1) for _ in range(self.num_objetos)]
            poblacion.append(individuo)
        
        return poblacion
    
    """def generar_poblacion_inicial(self):
        #Genera una población inicial de individuos aleatorios
        poblacion = []
        for _ in range(self.tam_poblacion):
            # Crear un individuo aleatorio con bits 0 o 1
            individuo = [random.randint(0, 1) for _ in range(self.num_objetos)]
            poblacion.append(individuo)
        return poblacion"""

    def evaluar_aptitud(self, individuo):
        """Evalúa la aptitud de un individuo"""
        peso_total = sum(self.pesos[i] for i in range(self.num_objetos) if individuo[i] == 1)
        
        if peso_total > self.peso_maximo:
            return 0  # Penalización fuerte para soluciones no factibles
        
        valor_total = sum(self.valores[i] for i in range(self.num_objetos) if individuo[i] == 1)
        
        if self.metodo_aptitud == "valor":
            return valor_total
        elif self.metodo_aptitud == "valor_cantidad":
            cantidad = sum(individuo)
            bonificacion = self.factor_cantidad * cantidad * self.valor_promedio
            return valor_total + bonificacion
        
        return valor_total
    
    def seleccion_torneo(self, poblacion, aptitudes, k=3):
        """Selección por torneo - más efectiva que elitista pura"""
        seleccionados = []
        for _ in range(len(poblacion)):
            # Seleccionar k individuos al azar para el torneo
            candidatos = random.sample(list(zip(poblacion, aptitudes)), k)
            # Elegir el mejor del torneo
            ganador = max(candidatos, key=lambda x: x[1])
            seleccionados.append(ganador[0])
        return seleccionados
    
    def cruce_uniforme(self, padre1, padre2):
        """Cruce uniforme - mejor para problemas de mochila"""
        if random.random() > self.prob_cruce:
            return padre1.copy(), padre2.copy()
        
        hijo1, hijo2 = [], []
        for i in range(len(padre1)):
            if random.random() < 0.5:
                hijo1.append(padre1[i])
                hijo2.append(padre2[i])
            else:
                hijo1.append(padre2[i])
                hijo2.append(padre1[i])
        
        return hijo1, hijo2
    
    def mutacion(self, individuo):
        """Mutación con reparación inteligente"""
        individuo_mutado = individuo.copy()
        
        for i in range(len(individuo_mutado)):
            if random.random() < self.prob_mutacion:
                individuo_mutado[i] = 1 - individuo_mutado[i]
        
        # Reparación: si excede peso, quitar objetos de menor ratio
        peso_actual = sum(self.pesos[i] for i in range(self.num_objetos) if individuo_mutado[i] == 1)
        if peso_actual > self.peso_maximo:
            # Obtener objetos seleccionados ordenados por ratio valor/peso
            objetos_seleccionados = [(i, self.valores[i]/self.pesos[i]) for i in range(self.num_objetos) if individuo_mutado[i] == 1]
            objetos_seleccionados.sort(key=lambda x: x[1])  # Menor ratio primero
            
            # Quitar objetos hasta que sea factible
            for idx, _ in objetos_seleccionados:
                individuo_mutado[idx] = 0
                peso_actual -= self.pesos[idx]
                if peso_actual <= self.peso_maximo:
                    break
        
        return individuo_mutado
    
    def evolucionar(self):
        """Ejecuta el algoritmo genético"""
        poblacion = self.generar_poblacion_inicial()
        
        print("\n---- Población Inicial ----")
        aptitudes_iniciales = [self.evaluar_aptitud(individuo) for individuo in poblacion]
        for i in range(min(4, len(poblacion))):  # Mostrar solo los primeros 4
            print(f"Individuo {i+1}: {poblacion[i]}, Aptitud: {aptitudes_iniciales[i]}")

        for generacion in range(self.num_generaciones):
            # Evaluar aptitudes
            aptitudes = [self.evaluar_aptitud(ind) for ind in poblacion]
            
            # Actualizar mejor solución
            mejor_idx = aptitudes.index(max(aptitudes))
            if aptitudes[mejor_idx] > self.mejor_aptitud:
                self.mejor_individuo = poblacion[mejor_idx].copy()
                self.mejor_aptitud = aptitudes[mejor_idx]
            
            self.historico_aptitud.append(max(aptitudes))
            
            # Mostrar progreso cada 20 generaciones
            if generacion % 10 == 0:
                mejor_valor = sum(self.valores[i] for i in range(self.num_objetos) if poblacion[mejor_idx][i] == 1)
                mejor_cantidad = sum(poblacion[mejor_idx])
                print(f"Gen {generacion}: Aptitud={max(aptitudes):.1f}, Valor={mejor_valor}, Objetos={mejor_cantidad}")
            
            # Crear nueva población
            nueva_poblacion = []
            
            # Elitismo: mantener los 2 mejores
            indices_ordenados = sorted(range(len(aptitudes)), key=lambda i: aptitudes[i], reverse=True)
            nueva_poblacion.extend([poblacion[indices_ordenados[0]], poblacion[indices_ordenados[1]]])
            
            # Selección por torneo
            padres = self.seleccion_torneo(poblacion, aptitudes)
            
            # Generar descendientes
            while len(nueva_poblacion) < self.tam_poblacion:
                padre1, padre2 = random.sample(padres, 2)
                hijo1, hijo2 = self.cruce_uniforme(padre1, padre2)
                
                hijo1 = self.mutacion(hijo1)
                hijo2 = self.mutacion(hijo2)
                
                nueva_poblacion.append(hijo1)
                if len(nueva_poblacion) < self.tam_poblacion:
                    nueva_poblacion.append(hijo2)
            
            poblacion = nueva_poblacion
        
        return self.mejor_individuo, self.mejor_aptitud
    
    def mostrar_resultados(self):
        """Muestra los resultados finales"""
        if self.mejor_individuo is None:
            print("No se ha ejecutado el algoritmo.")
            return
        
        valor_total = sum(self.valores[i] for i in range(self.num_objetos) if self.mejor_individuo[i] == 1)
        peso_total = sum(self.pesos[i] for i in range(self.num_objetos) if self.mejor_individuo[i] == 1)
        cantidad = sum(self.mejor_individuo)
        
        print(f"\n--- RESULTADO FINAL ---")
        print(f"Solución: {self.mejor_individuo}")
        print(f"Valor total: {valor_total}")
        print(f"Peso total: {peso_total}/{self.peso_maximo}")
        print(f"Objetos seleccionados: {cantidad}")
        print(f"Aptitud: {self.mejor_aptitud:.2f}")
        
        # Mostrar objetos seleccionados
        objetos_sel = [i+1 for i in range(self.num_objetos) if self.mejor_individuo[i] == 1]
        print(f"Objetos: {objetos_sel}")
        print("\nDetalle de objetos seleccionados:")
        print("Objeto | Peso | Valor")
        print("-"*20)
        for i in range(self.num_objetos):
            if self.mejor_individuo[i] == 1:
                print(f"{i+1:6d} | {self.pesos[i]:4d} | {self.valores[i]:5d}")


         # Mostrar análisis según método de aptitud
        if peso_total == self.peso_maximo:
            if self.metodo_aptitud == "valor":
                print("✓ CAPACIDAD MÁXIMA UTILIZADA - ALTO VALOR")
            else:
                print("✓ CAPACIDAD MÁXIMA UTILIZADA - ALTO VALOR Y MAYOR CANTIDAD DE OBJETOS")
        else:
            porcentaje_usado = (peso_total / self.peso_maximo) * 100
            if self.metodo_aptitud == "valor":
                print(f"Capacidad usada: {porcentaje_usado:.1f}% - Optimizada para valor")
            else:
                print(f"Capacidad usada: {porcentaje_usado:.1f}% - Balance valor-cantidad")
    
    def graficar_evolucion(self):
        """Grafica la evolución de la aptitud"""
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(self.historico_aptitud)), self.historico_aptitud, 'b-', linewidth=2)
        plt.title('Evolución de la Aptitud')
        plt.xlabel('Generación')
        plt.ylabel('Aptitud')
        plt.grid(True, alpha=0.3)
        plt.show()


def main():
    # Datos de prueba predeterminados
    usar_predeterminados = input("¿Usar datos predeterminados? (s/n): ").lower() == 's'
    
    if usar_predeterminados:
        pesos = [4, 2, 3, 1, 2, 5, 3]
        valores = [10, 4, 7, 1, 2, 8, 6]
        peso_maximo = 15
        print(f"Usando datos: pesos={pesos}, valores={valores}, peso_max={peso_maximo}")
    else:
        num_objetos = int(input("Ingrese número de objetos: "))
        pesos, valores = [], []
        for i in range(num_objetos):
            p, v = map(int, input(f"Objeto {i+1} (peso valor): ").split())
            pesos.append(p)
            valores.append(v)
        peso_maximo = int(input("Peso máximo: "))
    
    # Configuración del algoritmo genético
    tam_poblacion = int(input("Ingrese el tamaño de la población (recomendado: 50): ") or "50")
    num_generaciones = int(input("Ingrese el número de generaciones (recomendado: 100): ") or "100")
    prob_cruce = float(input("Ingrese la probabilidad de cruce (0-1, recomendado: 0.8): ") or "0.8")
    prob_mutacion = float(input("Ingrese la probabilidad de mutación \n0.01: Poca Exploracion, \n0.1: Balanceada, \n0.15: Mas Exploratoria, \n0.3: Muy Exploratoria, recomendado: 0.15: ") or "0.15")

    # Mostrar ratios para referencia, esto es por si se quiere ver que objeto es mas eficiente que otro
    # Un objeto es ineficiente si su ratio es menor que 1, esto es porque su peso es mayor que su valor
    # Ocupa mucha capadidad para poco valor
    """print("\nRatios valor/peso:")
    for i in range(len(pesos)):
        ratio = valores[i] / pesos[i]
        print(f"Objeto {i+1}: {ratio:.2f}")"""
    
    # Método de aptitud
    print("\nSeleccione el método de aptitud:")
    print("\n1. Solo valor\n2. Valor + cantidad")
    opcion = int(input("Método (1 o 2): "))
    
    metodo = "valor" if opcion == 1 else "valor_cantidad"
    factor = 0.2 if opcion == 2 else 0
    
    # Crear y ejecutar algoritmo
    ag = AlgoritmoGeneticoMochila(
        pesos, valores, peso_maximo,
        tam_poblacion,  # Población más grande
        prob_cruce,
        prob_mutacion,  # Mutación ligeramente mayor
        num_generaciones,  # Más generaciones
        metodo_aptitud=metodo,
        factor_cantidad=factor
    )
    
    tiempo_inicio = time.time()
    ag.evolucionar()
    tiempo_fin = time.time()
    
    ag.mostrar_resultados()
    print(f"Tiempo: {tiempo_fin - tiempo_inicio:.3f}s")
    
    try:
        ag.graficar_evolucion()
    except:
        print("No se pudo mostrar gráfico")


if __name__ == "__main__":
    main()