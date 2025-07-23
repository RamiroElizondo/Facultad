import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from Unidades.analisis_exploratorio import AnalisisExploratorio
from Unidades.regresion_lineal import RegresionLineal

def graficar_variables(df):
    # Configuración general
    plt.style.use("ggplot")
    sns.set_theme()
    OUTPUT_DIR = "poblacionGeneral"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Recorrer columnas
    for col in df.columns:
        plt.figure(figsize=(10, 5))
        
        # Si es numérica (int o float)
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col].dropna(), kde=True, bins=30)
            plt.title(f"Histograma de {col}")
            plt.xlabel(col)
            plt.ylabel("Frecuencia")

        # Si es booleana
        elif pd.api.types.is_bool_dtype(df[col]):
            sns.countplot(x=df[col])
            plt.title(f"Conteo de {col}")
            plt.xlabel(col)
            plt.ylabel("Cantidad")

        # Si es categórica (string u object)
        elif pd.api.types.is_object_dtype(df[col]) or df[col].nunique() < 30:
            orden = df[col].value_counts().index
            sns.countplot(y=df[col], order=orden)
            plt.title(f"Frecuencia de categorías en {col}")
            plt.xlabel("Cantidad")
            plt.ylabel(col)
        
        else:
            print(f"⚠️ No se pudo graficar la columna: {col}")
            continue

        # Guardar la imagen
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/{col}.png")
        plt.close()

    print(f"✅ Gráficos guardados en la carpeta: {OUTPUT_DIR}")

def main():
    """
    Función principal que gestiona el menú de opciones.
    """
    # Ruta del dataset (ajustar si es necesario)
    ruta_csv = "poblacion_2.csv"
    data = pd.read_csv(ruta_csv)
    # Crear instancia de la clase AnalisisExploratorio
    variables = [
            "Edad", 
            "Conteo_de_Globulos_blancos", 
            "Conteo_de_Globulos_rojos",
            "Conteo_de_Plaquetas", 
            "Nivel_de_Hemoglobina", 
            "Blastos_de_Médula_Osea", 
            "IMC"
            ]
    

    print("Atributos (encabezados):")
    for idx, col in enumerate(data.columns, start=1):
        print(f"  {idx:>2}. {col}")

    # --- 3. Cantidad de datos ---
    print(f"\nNúmero total de registros: {len(data):,}")
    graficar_variables(data)

    """while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Analisis Exploratorio")
        print("2. Estimacion por intervalos")
        print("3. Prueba de hipotesis")
        print("4. Regresion lineal")
        
        
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            analisis = AnalisisExploratorio(data)
            analisis.menu()
        if opcion == "4":
            
            print("\n---- Variables Disponibles ----")
            for i, var in enumerate(variables, start=1):
                print(f"{i}. {var}")
            print("-------------------------------")
            variable_x = input("Ingrese el nombre de la variable independiente: ")
            variable_y = input("Ingrese el nombre de la variable dependiente: ")
            regresion = RegresionLineal(data, variable_x, variable_y)
            regresion.menu()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")"""
    

if __name__ == "__main__":
    graficar_variables(pd.read_csv("biased_leukemia_dataset.csv"))
