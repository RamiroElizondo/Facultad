import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os


RUTA_CSV   = "water_potability.csv"     # ← Cambiá si tu archivo tiene otro nombre
CARPETA_QQ = "qq_plots"            # Carpeta donde se guardarán las imágenes
MUESTRA_MAX = 5000                 # Shapiro y Q-Q: limitar a 5k para no saturar

df = pd.read_csv(RUTA_CSV)

numericas = df.select_dtypes(include=["number"]).columns.difference(["ID_Paciente"])

# -----------------------------------------------------------
# 4. CREAR CARPETA DE SALIDA
# -----------------------------------------------------------
os.makedirs(CARPETA_QQ, exist_ok=True)

# -----------------------------------------------------------
# 5. GENERAR Q-Q PLOTS
# -----------------------------------------------------------
for col in numericas:
    serie = df[col].dropna()
    if len(serie) > MUESTRA_MAX:
        serie = serie.sample(MUESTRA_MAX, random_state=42)

    plt.figure(figsize=(6, 4))
    stats.probplot(serie, dist="norm", plot=plt)
    plt.title(f"Q-Q plot de {col}")
    plt.tight_layout()
    plt.savefig(f"{CARPETA_QQ}/qqplot_{col}.png")
    plt.close()

print(f"✅ Q-Q plots guardados en la carpeta: {CARPETA_QQ}")
