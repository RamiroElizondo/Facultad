import pygad
import numpy as np
import matplotlib.pyplot as plt

# 1. Ingreso de datos
def ingresar_datos():
    n = int(input("Cantidad de objetos: "))
    items = []
    for i in range(n):
        peso = int(input(f"Ingresar peso del objeto {i+1}: "))
        valor = int(input(f"Ingresar valor del objeto {i+1}: "))
        items.append((peso, valor))
    peso_max = int(input("Ingresar peso máximo de la mochila: "))
    return items, peso_max

items, peso_maximo = ingresar_datos()

# 2. Función de aptitud
def fitness_func(ga_instance, solution, solution_idx):
    peso_total = 0
    valor_total = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            peso_total += items[i][0]
            valor_total += items[i][1]
    if peso_total > peso_maximo:
        return 0
    return valor_total

# 3. Configurar AG
num_genes = len(items)

ga_instance = pygad.GA(
    num_generations=50,
    num_parents_mating=4,
    fitness_func=fitness_func,
    sol_per_pop=10,
    num_genes=num_genes,
    init_range_low=0,
    init_range_high=2,
    gene_type=int,
    mutation_percent_genes=20,
    stop_criteria=["reach_100"]
)

# 4. Ejecutar AG
ga_instance.run()

# 5. Resultados
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("\n Mejor solución encontrada:")
print("Representación binaria:", solution)
print("Valor total:", solution_fitness)

peso_total = sum(items[i][0] for i in range(len(solution)) if solution[i] == 1)
print("Peso total:", peso_total)

objetos_llevados = [i + 1 for i in range(len(solution)) if solution[i] == 1]
print("Objetos seleccionados:", objetos_llevados)

# 6. Visualización
plt.figure(figsize=(10, 5))
plt.plot(ga_instance.best_solutions_fitness, marker='o', color='green')
plt.title("Evolución del Valor de la Mochila")
plt.xlabel("Generación")
plt.ylabel("Fitness (valor total)")
plt.grid(True)
plt.tight_layout()
plt.show()


"""
7
4
10
2
4
3
7
1
1
2
2
5
8
3
6
15
"""