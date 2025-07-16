import matplotlib.pyplot as plt

# Datos
hilos = [2, 4, 6, 7]
tiempos = [0.0014820000, 0.001625667, 0.001344333, 0.001215667]
speedup = [2.1286549708, 1.940537216, 2.346640218, 2.595009597]
eficiencia = [1.0643274854, 0.485134304, 0.391106703, 0.370715657]


# 1. Tiempo promedio
plt.figure(figsize=(10, 5))
plt.plot(hilos, tiempos, marker='o')
plt.title('Tiempo Promedio vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Tiempo Promedio (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 1000/tiempo_promedio_vs_hilosMPI.png")

# 2. Speedup
plt.figure(figsize=(10, 5))
plt.plot(hilos, speedup, marker='o', color='green')
plt.title('Speedup vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Speedup')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/MPI/Para N 1000/speedup_vs_hilosMP.png")

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
plt.savefig("./Graficos/MPI/Para N 1000/eficiencia_vs_hilosMPI.png")
