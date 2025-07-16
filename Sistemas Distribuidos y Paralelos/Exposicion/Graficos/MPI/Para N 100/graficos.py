import matplotlib.pyplot as plt

# Datos
hilos = [2, 4, 6, 7]
tiempos = [0.0001963333, 0.000754667, 0.000221667, 0.000237667]
speedup = [0.6926994907, 0.180212014, 0.613533835, 0.572230014]
eficiencia = [0.3463497453, 0.045053004, 0.102255639, 0.081747145]



# 1. Tiempo promedio
plt.figure(figsize=(10, 5))
plt.plot(hilos, tiempos, marker='o')
plt.title('Tiempo Promedio vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Tiempo Promedio (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 100/tiempo_promedio_vs_hilosMPI.png")

# 2. Speedup
plt.figure(figsize=(10, 5))
plt.plot(hilos, speedup, marker='o', color='green')
plt.title('Speedup vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Speedup')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 100/speedup_vs_hilosMPI.png")

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
plt.savefig("./Graficos/MPI/Para N 100/eficiencia_vs_hilosMPI.png")
