import random
import time
import matplotlib.pyplot as plt

class AlgoritmoGeneticoMochila:
    def __init__(self, pesos, valores, peso_maximo, tam_poblacion=50, prob_cruce=0.8, 
                 prob_mutacion=0.1, num_generaciones=100, metodo_aptitud="valor", factor_cantidad=0.2):
        """
        Inicializa el algoritmo genético para el problema de la mochila
        
        Parámetros:
        pesos: lista de pesos de los objetos
        valores: lista de valores de los objetos
        peso_maximo: capacidad máxima de la mochila
        tam_poblacion: tamaño de la población
        prob_cruce: probabilidad de cruce
        prob_mutacion: probabilidad de mutación
        num_generaciones: número máximo de generaciones
        metodo_aptitud: "valor" (solo valor) o "valor_cantidad" (valor + cantidad)
        factor_cantidad: factor para bonificar la cantidad de objetos (0.0-1.0)
        """
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
        
        # Para almacenar resultados
        self.mejor_individuo = None
        self.mejor_aptitud = 0
        self.historico_aptitud = []
        self.poblacion_actual = []
        
        # Calcular valores de referencia para normalización
        self.valor_maximo_teorico = sum(valores)
        self.valor_promedio_objeto = sum(valores) / len(valores) if valores else 0
        
        print(f"\nMétodo de aptitud seleccionado: {metodo_aptitud}")
        if metodo_aptitud == "valor_cantidad":
            print(f"Factor de bonificación por cantidad de objetos: {factor_cantidad}")
            print(f"Valor promedio por objeto: {self.valor_promedio_objeto:.2f}")
        else:
            print("Optimizando solo por valor total")
    
    def generar_poblacion_inicial(self):
        """Genera una población inicial de individuos aleatorios"""
        poblacion = []
        for _ in range(self.tam_poblacion):
            # Crear un individuo aleatorio con bits 0 o 1
            individuo = [random.randint(0, 1) for _ in range(self.num_objetos)]
            poblacion.append(individuo)
        return poblacion
    
    def evaluar_aptitud(self, individuo):
        """
        Evalúa la aptitud según el método seleccionado
        """
        peso_total = sum(self.pesos[i] for i in range(self.num_objetos) if individuo[i] == 1)
        
        # Si excede el peso máximo, solución no factible
        if peso_total > self.peso_maximo:
            return 0
        
        # Calcular valor total
        valor_total = sum(self.valores[i] for i in range(self.num_objetos) if individuo[i] == 1)
        
        if self.metodo_aptitud == "valor":
            # Solo considerar el valor total
            return valor_total
        
        elif self.metodo_aptitud == "valor_cantidad":
            # Considerar valor total + bonificación por cantidad
            cantidad_objetos = sum(individuo)
            bonificacion_cantidad = self.factor_cantidad * cantidad_objetos * self.valor_promedio_objeto
            return valor_total + bonificacion_cantidad
        
        else:
            # Por defecto, solo valor
            return valor_total
    
    def evaluar_aptitud_detallada(self, individuo):
        """
        Versión detallada para mostrar el desglose de la aptitud según el método
        """
        peso_total = sum(self.pesos[i] for i in range(self.num_objetos) if individuo[i] == 1)
        valor_total = sum(self.valores[i] for i in range(self.num_objetos) if individuo[i] == 1)
        cantidad_objetos = sum(individuo)
        
        if peso_total > self.peso_maximo:
            return {
                'aptitud_total': 0,
                'valor_total': valor_total,
                'cantidad_objetos': cantidad_objetos,
                'bonificacion_cantidad': 0,
                'peso_total': peso_total,
                'factible': False,
                'metodo': self.metodo_aptitud
            }
        
        if self.metodo_aptitud == "valor":
            return {
                'aptitud_total': valor_total,
                'valor_total': valor_total,
                'cantidad_objetos': cantidad_objetos,
                'bonificacion_cantidad': 0,
                'peso_total': peso_total,
                'factible': True,
                'metodo': self.metodo_aptitud
            }
        
        elif self.metodo_aptitud == "valor_cantidad":
            bonificacion_cantidad = self.factor_cantidad * cantidad_objetos * self.valor_promedio_objeto
            aptitud_total = valor_total + bonificacion_cantidad
            
            return {
                'aptitud_total': aptitud_total,
                'valor_total': valor_total,
                'cantidad_objetos': cantidad_objetos,
                'bonificacion_cantidad': bonificacion_cantidad,
                'peso_total': peso_total,
                'factible': True,
                'metodo': self.metodo_aptitud
            }
        
        else:
            # Por defecto, solo valor
            return {
                'aptitud_total': valor_total,
                'valor_total': valor_total,
                'cantidad_objetos': cantidad_objetos,
                'bonificacion_cantidad': 0,
                'peso_total': peso_total,
                'factible': True,
                'metodo': self.metodo_aptitud
            }
    
    def seleccion_elitista(self, poblacion, aptitudes):
        """
        Realiza la selección elitista, ordenando la población por aptitud
        y seleccionando los mejores individuos
        """
        # Crear pares (aptitud, individuo) y ordenarlos de mayor a menor aptitud
        pares = list(zip(aptitudes, poblacion))
        pares.sort(reverse=True, key=lambda x: x[0])
        
        # Extraer los individuos ordenados
        poblacion_ordenada = [individuo for _, individuo in pares]
        
        # Devolver la población ordenada por aptitud
        return poblacion_ordenada
    
    def cruce_un_punto(self, padre1, padre2):
        """Realiza el cruce de un punto entre dos padres"""
        if random.random() > self.prob_cruce:
            return padre1.copy(), padre2.copy()
        
        punto_cruce = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        
        return hijo1, hijo2
    
    def mutacion(self, individuo):
        """Aplica mutación a un individuo"""
        for i in range(len(individuo)):
            if random.random() < self.prob_mutacion:
                individuo[i] = 1 - individuo[i]  # Invertir bit (0->1, 1->0)
        return individuo
    
    def evolucionar(self):
        """Ejecuta el algoritmo genético"""
        # Generar población inicial
        poblacion = self.generar_poblacion_inicial()
        self.poblacion_actual = poblacion
        
        # Para visualización: mostrar población inicial
        print(f"\n---- Población Inicial (Método: {self.metodo_aptitud}) ----")
        for i in range(min(4, len(poblacion))):
            detalles = self.evaluar_aptitud_detallada(poblacion[i])
            print(f"Individuo {i+1}: {poblacion[i]}")
            if self.metodo_aptitud == "valor":
                print(f"  Valor: {detalles['valor_total']}, Objetos: {detalles['cantidad_objetos']}, "
                      f"Aptitud: {detalles['aptitud_total']}")
            else:
                print(f"  Valor: {detalles['valor_total']}, Objetos: {detalles['cantidad_objetos']}, "
                      f"Bonificación: {detalles['bonificacion_cantidad']:.2f}, "
                      f"Aptitud total: {detalles['aptitud_total']:.2f}")
        
        # Evolución a través de generaciones
        for generacion in range(self.num_generaciones):
            # Evaluar aptitud de cada individuo
            aptitudes = [self.evaluar_aptitud(individuo) for individuo in poblacion]
            
            # Encontrar el mejor individuo
            mejor_idx = aptitudes.index(max(aptitudes))
            if aptitudes[mejor_idx] > self.mejor_aptitud:
                self.mejor_individuo = poblacion[mejor_idx].copy()
                self.mejor_aptitud = aptitudes[mejor_idx]
            
            # Almacenar para histórico
            self.historico_aptitud.append(max(aptitudes))
            
            # Mostrar progreso
            if generacion % 10 == 0:
                mejor_detalles = self.evaluar_aptitud_detallada(poblacion[mejor_idx])
                if self.metodo_aptitud == "valor":
                    print(f"Generación {generacion}: Mejor aptitud = {max(aptitudes):.2f} "
                          f"(Valor: {mejor_detalles['valor_total']}, "
                          f"Objetos: {mejor_detalles['cantidad_objetos']})")
                else:
                    print(f"Generación {generacion}: Mejor aptitud = {max(aptitudes):.2f} "
                          f"(Valor: {mejor_detalles['valor_total']}, "
                          f"Objetos: {mejor_detalles['cantidad_objetos']}, "
                          f"Bonif: {mejor_detalles['bonificacion_cantidad']:.1f})")
            
            # Aplicar selección elitista
            poblacion_ordenada = self.seleccion_elitista(poblacion, aptitudes)
            
            # Crear nueva población
            nueva_poblacion = []
            
            # Elitismo: los mejores individuos pasan directamente
            num_elites = max(2, int(self.tam_poblacion * 0.1))
            nueva_poblacion.extend(poblacion_ordenada[:num_elites])
            
            # Completar la población con descendientes
            while len(nueva_poblacion) < self.tam_poblacion:
                # Seleccionar padres con probabilidad proporcional a su posición
                indices = list(range(len(poblacion_ordenada)))
                pesos_seleccion = [1/(i+1) for i in indices]
                
                idx1, idx2 = random.choices(indices, weights=pesos_seleccion, k=2)
                padre1, padre2 = poblacion_ordenada[idx1], poblacion_ordenada[idx2]
                
                # Cruzamiento
                hijo1, hijo2 = self.cruce_un_punto(padre1, padre2)
                
                # Mutación
                hijo1 = self.mutacion(hijo1)
                hijo2 = self.mutacion(hijo2)
                
                # Añadir a nueva población
                nueva_poblacion.append(hijo1)
                if len(nueva_poblacion) < self.tam_poblacion:
                    nueva_poblacion.append(hijo2)
            
            # Actualizar población
            poblacion = nueva_poblacion
            self.poblacion_actual = poblacion
        
        # Evaluar última generación
        aptitudes_finales = [self.evaluar_aptitud(individuo) for individuo in poblacion]
        mejor_idx = aptitudes_finales.index(max(aptitudes_finales))
        
        if aptitudes_finales[mejor_idx] > self.mejor_aptitud:
            self.mejor_individuo = poblacion[mejor_idx].copy()
            self.mejor_aptitud = aptitudes_finales[mejor_idx]
        
        return self.mejor_individuo, self.mejor_aptitud
    
    def mostrar_resultados(self):
        """Muestra los resultados del algoritmo genético con detalles de aptitud"""
        if self.mejor_individuo is None:
            print("Todavía no se ha ejecutado el algoritmo.")
            return
        
        detalles = self.evaluar_aptitud_detallada(self.mejor_individuo)
        
        print("\n---- Resultados finales ----")
        print(f"Método utilizado: {detalles['metodo']}")
        print(f"Mejor solución encontrada: {self.mejor_individuo}")
        
        if self.metodo_aptitud == "valor":
            print(f"Aptitud (Valor total): {detalles['aptitud_total']}")
            print(f"Cantidad de objetos: {detalles['cantidad_objetos']}")
        else:
            print(f"Aptitud total: {detalles['aptitud_total']:.2f}")
            print(f"  - Valor total: {detalles['valor_total']}")
            print(f"  - Cantidad de objetos: {detalles['cantidad_objetos']}")
            print(f"  - Bonificación por cantidad: {detalles['bonificacion_cantidad']:.2f}")
        
        objetos_seleccionados = [i+1 for i in range(self.num_objetos) if self.mejor_individuo[i] == 1]
        
        print(f"Objetos seleccionados: {objetos_seleccionados}")
        print(f"Peso total: {detalles['peso_total']}/{self.peso_maximo}")
        
        print("\nDetalle de objetos seleccionados:")
        print("Objeto | Peso | Valor | Ratio Valor/Peso")
        print("-"*40)
        valor_total_check = 0
        peso_total_check = 0
        for i in range(self.num_objetos):
            if self.mejor_individuo[i] == 1:
                ratio = self.valores[i] / self.pesos[i]
                print(f"{i+1:6d} | {self.pesos[i]:4d} | {self.valores[i]:5d} | {ratio:12.2f}")
                valor_total_check += self.valores[i]
                peso_total_check += self.pesos[i]
        
        print(f"\nVerificación - Valor total: {valor_total_check}, Peso total: {peso_total_check}")
    
    def graficar_evolucion(self):
        """Grafica la evolución de la aptitud a lo largo de las generaciones"""
        plt.figure(figsize=(12, 8))
        
        # Gráfico principal de evolución
        plt.subplot(2, 1, 1)
        plt.plot(range(len(self.historico_aptitud)), self.historico_aptitud, 
                marker='o', linestyle='-', linewidth=2, markersize=3)
        
        if self.metodo_aptitud == "valor":
            plt.title('Evolución de la Aptitud (Solo Valor)')
            plt.ylabel('Valor Total')
        else:
            plt.title('Evolución de la Aptitud (Valor + Bonificación por Cantidad)')
            plt.ylabel('Aptitud Total')
        
        plt.xlabel('Generación')
        plt.grid(True, alpha=0.3)
        
        # Gráfico de componentes de aptitud para las últimas generaciones
        plt.subplot(2, 1, 2)
        ultimas_generaciones = min(20, len(self.historico_aptitud))
        generaciones = range(len(self.historico_aptitud) - ultimas_generaciones, len(self.historico_aptitud))
        aptitudes_recientes = self.historico_aptitud[-ultimas_generaciones:]
        
        plt.plot(generaciones, aptitudes_recientes, 'b-o', label='Aptitud Total', linewidth=2)
        plt.title(f'Detalle de las Últimas {ultimas_generaciones} Generaciones')
        plt.xlabel('Generación')
        plt.ylabel('Aptitud')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def comparar_metodos(self):
        """Compara diferentes métodos de evaluación de aptitud"""
        if self.mejor_individuo is None:
            print("Primero debe ejecutar el algoritmo.")
            return
        
        print("\n---- Análisis de la Solución ----")
        
        # Evaluar la solución actual
        detalles_actual = self.evaluar_aptitud_detallada(self.mejor_individuo)
        
        print(f"Método usado: {detalles_actual['metodo']}")
        print(f"Solución: {self.mejor_individuo}")
        print(f"Valor total: {detalles_actual['valor_total']}")
        print(f"Cantidad de objetos: {detalles_actual['cantidad_objetos']}")
        print(f"Peso total: {detalles_actual['peso_total']}/{self.peso_maximo}")
        
        if self.metodo_aptitud == "valor_cantidad":
            print(f"Bonificación por cantidad: {detalles_actual['bonificacion_cantidad']:.2f}")
            print(f"Aptitud total: {detalles_actual['aptitud_total']:.2f}")
            
            # Mostrar qué pasaría solo con valor
            print("\n-- Comparación con método 'solo valor' --")
            print(f"Si solo se considerara valor: {detalles_actual['valor_total']}")
            print(f"Diferencia por bonificación: +{detalles_actual['bonificacion_cantidad']:.2f}")
        
        # Calcular eficiencia
        if detalles_actual['cantidad_objetos'] > 0:
            eficiencia = detalles_actual['valor_total'] / detalles_actual['cantidad_objetos']
            print(f"\nEficiencia (Valor por objeto): {eficiencia:.2f}")
        
        # Mostrar ratio valor/peso de objetos seleccionados
        print("\nAnálisis de objetos seleccionados:")
        ratios = []
        for i in range(self.num_objetos):
            if self.mejor_individuo[i] == 1:
                ratio = self.valores[i] / self.pesos[i]
                ratios.append((i+1, ratio, self.valores[i], self.pesos[i]))
        
        ratios.sort(key=lambda x: x[1], reverse=True)
        print("Objeto | Ratio V/P | Valor | Peso")
        print("-"*35)
        for obj, ratio, valor, peso in ratios:
            print(f"{obj:6d} | {ratio:8.2f} | {valor:5d} | {peso:4d}")


def main():
    # Permitir ingresar datos desde teclado
    usar_predeterminados = input("¿Usar datos predeterminados? (s/n): ").lower() == 's'
    
    if usar_predeterminados:
        pesos = [15, 2, 3, 1, 2, 5, 3]
        valores = [31, 4, 7, 1, 2, 8, 6]
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
    
    # Selección del método de aptitud
    print("\nSeleccione el método de evaluación de aptitud:")
    print("1. Solo valor (maximizar valor total)")
    print("2. Valor + cantidad (maximizar valor y cantidad de objetos)")
    
    while True:
        try:
            opcion = int(input("Ingrese su opción (1 o 2): "))
            if opcion in [1, 2]:
                break
            else:
                print("Por favor, ingrese 1 o 2")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    if opcion == 1:
        metodo_aptitud = "valor"
        factor_cantidad = 0  # No se usa, pero se mantiene para compatibilidad
    else:
        metodo_aptitud = "valor_cantidad"
        factor_cantidad = float(input("Ingrese el factor de bonificación por cantidad de objetos (0.1-0.5, recomendado: 0.2): ") or "0.2")
    
    # Configuración del algoritmo genético
    tam_poblacion = int(input("Ingrese el tamaño de la población (recomendado: 50): ") or "50")
    num_generaciones = int(input("Ingrese el número de generaciones (recomendado: 100): ") or "100")
    prob_cruce = float(input("Ingrese la probabilidad de cruce (0-1, recomendado: 0.8): ") or "0.8")
    prob_mutacion = float(input("Ingrese la probabilidad de mutación (0-1, recomendado: 0.1): ") or "0.1")
    
    # Crear y ejecutar el algoritmo genético
    ag = AlgoritmoGeneticoMochila(
        pesos, valores, peso_maximo, 
        tam_poblacion, prob_cruce, prob_mutacion, num_generaciones, 
        metodo_aptitud, factor_cantidad
    )
    
    # Ejecutar el algoritmo
    tiempo_inicio = time.time()
    ag.evolucionar()
    tiempo_fin = time.time()
    
    # Mostrar resultados
    ag.mostrar_resultados()
    ag.comparar_metodos()
    print(f"\nTiempo de ejecución: {tiempo_fin - tiempo_inicio:.4f} segundos")
    
    # Graficar evolución
    try:
        ag.graficar_evolucion()
    except Exception as e:
        print(f"No se pudo generar el gráfico: {e}")
        print("Puede ser necesario instalar matplotlib o ejecutar en un entorno que soporte gráficos.")


if __name__ == "__main__":
    main()