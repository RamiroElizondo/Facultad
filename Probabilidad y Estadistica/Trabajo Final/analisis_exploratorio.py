import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

class Analisis_exploratorio:
    def __init__(self, id,data):
        self.id = id
        self.data = data

    def estadisticas_descriptivas(self):
        num_cols = self.data.select_dtypes(include=["number"]).columns.tolist()
        
        stats = self.data[num_cols].agg(["mean", "var", "std", "skew", "kurt"]).T
        stats.columns = [
            "Media_Poblacion1", 
            "Varianza_Poblacion1", 
            "DesvStd_Poblacion1", 
            "Asimetría", 
            "Curtosis"
        ]
        conclusiones_asimetria = []
        conclusiones_curtosis = []

        for i, row in stats.iterrows():
            # Asimetría
            if abs(row["Asimetría"]) < 0.1:
                conclusiones_asimetria.append("Simétrica")
            elif row["Asimetría"] > 0:
                conclusiones_asimetria.append("Asimetría positiva (cola derecha)")
            else:
                conclusiones_asimetria.append("Asimetría negativa (cola izquierda)")

            # Curtosis
            if abs(row["Curtosis"]) < 0.1:
                conclusiones_curtosis.append("Curtosis normal (mesocúrtica)")
            elif row["Curtosis"] > 0:
                conclusiones_curtosis.append("Curtosis alta (leptocúrtica)")
            else:
                conclusiones_curtosis.append("Curtosis baja (platicúrtica)")

        stats["Conclusión_Asimetría"] = conclusiones_asimetria
        stats["Conclusión_Curtosis"] = conclusiones_curtosis
        print(stats.round(4))

    def graficar_variables(self):
        plt.style.use("ggplot")
        sns.set_theme()

        # Seleccionar variables numéricas (excluyendo ID si está)
        numericas = self.data.select_dtypes(include=["number"]).columns.difference(["ID_Paciente"])

        n = len(numericas)
        fig, axs = plt.subplots(2, n, figsize=(5 * n, 8))  # 2 filas, N columnas

        for i, col in enumerate(numericas):
            datos = self.data[col].dropna()

            # Fila superior: histograma
            sns.histplot(datos, kde=True, bins=30, ax=axs[0, i])
            axs[0, i].set_title(f"Histograma de {col}")
            axs[0, i].set_xlabel("")
            axs[0, i].set_ylabel("Frecuencia")

            # Fila inferior: Q-Q plot
            stats.probplot(datos, dist="norm", plot=axs[1, i])
            axs[1, i].set_title(f"Q-Q plot de {col}")

        plt.tight_layout()
        plt.show()

    def guardar_graficos(self):
        print("Creando gráficos y guardándolos como imágenes...")

        # Configuración general
        plt.style.use("ggplot")
        sns.set_theme()
        OUTPUT_DIR = "Graficos_Poblacion" + str(self.id)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        for col in self.data.columns:
            serie = self.data[col].dropna()

            # Si es numérica (int o float)
            if pd.api.types.is_numeric_dtype(serie):
                # Histograma
                plt.figure(figsize=(10, 5))
                sns.histplot(serie, kde=True, bins=30)
                plt.title(f"Histograma de {col}")
                plt.xlabel(col)
                plt.ylabel("Frecuencia")
                plt.tight_layout()
                plt.savefig(f"{OUTPUT_DIR}/Hist_{col}.png")
                plt.close()

                # Q-Q Plot
                plt.figure(figsize=(6, 6))
                stats.probplot(serie, dist="norm", plot=plt)
                plt.title(f"Q-Q Plot de {col}")
                plt.tight_layout()
                plt.savefig(f"{OUTPUT_DIR}/QQ_{col}.png")
                plt.close()

            # Si es booleana
            elif pd.api.types.is_bool_dtype(serie):
                plt.figure(figsize=(8, 4))
                sns.countplot(x=serie)
                plt.title(f"Conteo de {col}")
                plt.xlabel(col)
                plt.ylabel("Cantidad")
                plt.tight_layout()
                plt.savefig(f"{OUTPUT_DIR}/{col}.png")
                plt.close()

            # Si es categórica (menos de 30 categorías)
            elif pd.api.types.is_object_dtype(serie) or self.data[col].nunique() < 30:
                plt.figure(figsize=(8, 5))
                orden = serie.value_counts().index
                sns.countplot(y=serie, order=orden)
                plt.title(f"Frecuencia de categorías en {col}")
                plt.xlabel("Cantidad")
                plt.ylabel(col)
                plt.tight_layout()
                plt.savefig(f"{OUTPUT_DIR}/{col}.png")
                plt.close()

            else:
                print(f"No se pudo graficar la columna: {col}")
                continue

        print(f"Gráficos guardados en la carpeta: {OUTPUT_DIR}")