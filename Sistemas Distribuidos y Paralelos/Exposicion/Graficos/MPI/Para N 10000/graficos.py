import matplotlib.pyplot as plt

# Datos
hilos = [2, 4, 6, 7]
tiempos = [0.1430100000, 0.077319667, 0.051032333, 0.042844000]
speedup = [1.9967391558, 3.693156980, 5.595544002, 6.664962811]
eficiencia = [0.9983695779, 0.923289245, 0.932590667, 0.952137544]


# 1. Tiempo promedio
plt.figure(figsize=(10, 5))
plt.plot(hilos, tiempos, marker='o')
plt.title('Tiempo Promedio vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Tiempo Promedio (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 10000/tiempo_promedio_vs_hilosMPI.png")

# 2. Speedup
plt.figure(figsize=(10, 5))
plt.plot(hilos, speedup, marker='o', color='green')
plt.title('Speedup vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Speedup')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 10000/speedup_vs_hilosMP.png")

# 3. Eficiencia
plt.figure(figsize=(10, 5))
plt.plot(hilos, eficiencia, marker='o', color='orange')
plt.axhline(0.5, linestyle='--', color='red', label='Umbral de eficiencia (0.5)')
plt.title('Eficiencia vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Eficiencia')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 10000/eficiencia_vs_hilosMPI.png")
