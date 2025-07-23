import pandas as pd
import os

# Cargar el archivo CSV original
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_CSV_POB1 = os.path.join(BASE_DIR, "poblacionINDIA.csv")
df = pd.read_csv(RUTA_CSV_POB1)

# Extraer solo la columna deseada
variable = input("Ingrese el nombre de la columna que desea extraer: ")
variable = variable.strip()  # Eliminar espacios en blanco al inicio y al final
if variable not in df.columns:
    print(f"La columna '{variable}' no existe en el DataFrame.")
else:
    sample = df[variable].dropna().sample(1023, random_state=42)

    sample_df = pd.DataFrame(sample)
    # Guardar el DataFrame en un nuevo archivo CSV
    sample_df.to_csv(f'{variable}.csv', index=False)