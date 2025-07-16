import matplotlib.pyplot as plt

# Datos
# Datos
hilos = [2, 4, 8, 12]
tiempos = [0.0030745403, 0.004195787, 0.003610479, 0.003850382]
speedup = [0.5875132987, 0.430511175, 0.500302915, 0.469130901]
eficiencia = [0.2937566494, 0.107627794, 0.062537864, 0.039094242]

# 1. Tiempo promedio
plt.figure(figsize=(10, 5))
plt.plot(hilos, tiempos, marker='o')
plt.title('Tiempo Promedio vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Tiempo Promedio (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/OpenMP/Para N 1000/tiempo_promedio_vs_hilos.png")

# 2. Speedup
plt.figure(figsize=(10, 5))
plt.plot(hilos, speedup, marker='o', color='green')
plt.title('Speedup vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Speedup')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/OpenMP/Para N 1000/speedup_vs_hilos.png")


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
plt.savefig("./Graficos/OpenMP/Para N 1000/eficiencia_vs_hilos.png")
