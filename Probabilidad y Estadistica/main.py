import pandas as pd

from Unidades.analisis_exploratorio import AnalisisExploratorio
from Unidades.regresion_lineal import RegresionLineal


def main():
    """
    Función principal que gestiona el menú de opciones.
    """
    # Ruta del dataset (ajustar si es necesario)
    ruta_csv = "biased_leukemia_dataset.csv"
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
    
    while True:
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
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
