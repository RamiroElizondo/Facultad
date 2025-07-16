import matplotlib.pyplot as plt

# Datos
hilos = [2, 4, 6, 7]
tiempos = [0.0000642807, 0.002969600, 0.000234275, 0.000365194]

speedup= [29.0201304695, 0.628176564, 7.962568260, 5.108061286]

eficiencia = [14.5100652348, 0.157044141, 0.995321033, 0.425671774]

# 1. Tiempo promedio
plt.figure(figsize=(10, 5))
plt.plot(hilos, tiempos, marker='o')
plt.title('Tiempo Promedio vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Tiempo Promedio (s)')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/OpenMP/Para N 10/tiempo_promedio_vs_hilos.png")

# 2. Speedup
plt.figure(figsize=(10, 5))
plt.plot(hilos, speedup, marker='o', color='green')
plt.title('Speedup vs Número de Hilos')
plt.xlabel('Número de Hilos')
plt.ylabel('Speedup')
plt.grid(True)
plt.tight_layout()
plt.savefig("./Graficos/OpenMP/Para N 10/speedup_vs_hilos.png")

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
plt.savefig("./Graficos/OpenMP/Para N 10/eficiencia_vs_hilos.png")
