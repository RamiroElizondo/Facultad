import pandas as pd
import os

# Cargar el archivo CSV original
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV_POB1 = os.path.join(BASE_DIR, "poblacionUSA.csv")
df = pd.read_csv(RUTA_CSV_POB1)

# Extraer solo la columna deseada
#contar cuantas positivos hay en la columna "Estado_de_Leucemia"
def extraer_columna_estado_positivo(df):
    if "Estado_de_Leucemia" in df.columns:
        return df["Estado_de_Leucemia"].value_counts().get("Positive", 0)
    else:
        raise ValueError("La columna 'Estado_de_Leucemia' no existe en el DataFrame.")
print(extraer_columna_estado_positivo(df))

23083
22777