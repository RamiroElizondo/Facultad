import matplotlib.pyplot as plt

# Datos del problema
objetos = [(4,10), (2,4), (3,7), (1,1), (2,2), (5,8), (3,6)]
nombres = [f"Obj {i+1}" for i in range(len(objetos))]

# Leer datos desde archivo
archivo = "soluciones.txt"
with open(archivo, "r") as f:
    lineas = f.readlines()

# Procesar líneas para extraer valores por iteración
mejores_valores = []
for linea in lineas:
    if "Mejor hasta ahora:" in linea:
        partes = linea.strip().split("-> Valor:")
        valor = int(partes[1].strip())
        mejores_valores.append(valor)

# Obtener la mejor solución final
for linea in reversed(lineas):
    if ">> Mejor Solución Encontrada:" in linea:
        solucion_str = linea.strip().split(":")[1].split("->")[0].strip()
        solucion_final = [int(x) for x in solucion_str.strip("[]").split(",")]
        break

# =======================
# Gráfico 1: Progreso del valor
# =======================
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(mejores_valores) + 1), mejores_valores, marker='o', color='blue')
plt.title("Progreso de la mejor solución (valor)")
plt.xlabel("Iteración")
plt.ylabel("Valor")
plt.grid(True)
plt.xticks(range(1, len(mejores_valores) + 1))
plt.tight_layout()
plt.show()

# =======================
# Gráfico 2: Objetos seleccionados
# =======================
pesos_seleccionados = [objetos[i][0] for i in range(len(objetos)) if solucion_final[i]]
valores_seleccionados = [objetos[i][1] for i in range(len(objetos)) if solucion_final[i]]
nombres_seleccionados = [nombres[i] for i in range(len(objetos)) if solucion_final[i]]

plt.figure(figsize=(8, 5))
plt.bar(nombres_seleccionados, valores_seleccionados, color='green')
plt.title("Objetos seleccionados en la mejor solución")
plt.xlabel("Objeto")
plt.ylabel("Valor")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
