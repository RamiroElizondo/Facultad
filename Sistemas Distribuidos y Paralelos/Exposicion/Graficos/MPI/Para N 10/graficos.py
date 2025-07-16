import matplotlib.pyplot as plt

# Datos
hilos = [2, 4, 6, 7]
tiempos = [0.0000993333, 0.000258333, 0.000199667, 0.000187667]

speedup = [0.1342281879, 0.051612903, 0.066777963, 0.071047957]

eficiencia = [0.0671140940, 0.012903226, 0.011129661, 0.010149708]


# 1. Tiempo promedio
plt.figure(figsize=(10, 5))
plt.plot(hilos, tiempos, marker='o')
plt.title('Tiempo Promedio vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Tiempo Promedio (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 10/tiempo_promedio_vs_hilosMPI.png")

# 2. Speedup
plt.figure(figsize=(10, 5))
plt.plot(hilos, speedup, marker='o', color='green')
plt.title('Speedup vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Speedup')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 10/speedup_vs_hilosMPI.png")

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
plt.savefig("./Graficos/MPI/Para N 10/eficiencia_vs_hilosMPI.png")
