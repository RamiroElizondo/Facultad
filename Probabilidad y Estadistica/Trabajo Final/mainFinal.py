import pandas as pd
from pathlib import Path
from dependencias import analizar_dependencias, prueba_dependencias, prueba_independencia
from analisis_exploratorio import Analisis_exploratorio
from normal import test_normalidad
from docimas import Docimas
import os

class Menu:
    def __init__(self):

        self.poblacion, self.pob1, self.pob2 = self.cargar_datasets()


    def mostrar_menu(self):
        print("\n=== Menú Principal ===")
        print("1. Análisis Exploratorio de Datos")
        print("2. Análisis de Normalidad")
        print("3. Docimas")
        print("4. Pruebas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            self.analisis_exploratorio()
        elif opcion == "2":
            self.analisis_normalidad()
        elif opcion == "3":
            self.docimas()
        elif opcion == "4":
            self.pruebas()
        elif opcion == "5":
            print("Saliendo del programa...")
            return False

    def dividir_dataset(self,df):
        # Cargar el dataset
        df = pd.read_csv("biased_leukemia_dataset.csv")

        # Mezclar aleatoriamente el dataset (sin modificar el original)
        df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

        # Dividir a la mitad
        n = len(df_shuffled) // 2
        poblacion_1 = df_shuffled.iloc[:n].copy()
        poblacion_2 = df_shuffled.iloc[n:].copy()

        print(f"Población 1: {len(poblacion_1)} registros")
        print(f"Población 2: {len(poblacion_2)} registros")

        poblacion_1.to_csv("poblacion_1.csv", index=False)
        poblacion_2.to_csv("poblacion_2.csv", index=False)

    def cargar_datasets(self):
        # Ruta del dataset original
        # Una vez dividido, cargamos las poblaciones
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        RUTA_CSV_ORIGINAL = os.path.join(BASE_DIR, "biased_leukemia_dataset.csv")
        RUTA_CSV_POB1 = os.path.join(BASE_DIR, "poblacion_1.csv")
        RUTA_CSV_POB2 = os.path.join(BASE_DIR, "poblacion_2.csv")
                        
        poblacion = pd.read_csv(RUTA_CSV_ORIGINAL)
        pob1 = pd.read_csv(RUTA_CSV_POB1)
        pob2 = pd.read_csv(RUTA_CSV_POB2)

        pob1.drop('ID_Paciente', axis=1, inplace=True)
        pob2.drop('ID_Paciente', axis=1, inplace=True)

        pd.set_option('display.float_format', '{:.5f}'.format)

        # Convertimos las columnas de conteo y hemoglobina a las unidades correctas
        # El conteo de glóbulos rojos se multiplica por 1,000,000
        pob1["Conteo_de_Globulos_rojos"] = pob1["Conteo_de_Globulos_rojos"] * 1000000
        pob2["Conteo_de_Globulos_rojos"] = pob2["Conteo_de_Globulos_rojos"] * 1000000

        # El nivel de hemoglobina se multiplica por 10, para pasar de la medidada gramos/decilitro a  gramos/litros
        pob1["Nivel_de_Hemoglobina"] = pob1["Nivel_de_Hemoglobina"] * 10
        pob2["Nivel_de_Hemoglobina"] = pob2["Nivel_de_Hemoglobina"] * 10
        
        return poblacion, pob1, pob2

    def analisis_exploratorio(self):
        print("\n=== Análisis de la Población 1 ===")
        objeto_analisis1 = Analisis_exploratorio(id=1,data=self.pob1)
        objeto_analisis1.estadisticas_descriptivas()
        objeto_analisis1.graficar_variables()

        print("\n=== Análisis de la Población 2 ===")
        objeto_analisis2 = Analisis_exploratorio(id=2,data=self.pob2)
        objeto_analisis2.estadisticas_descriptivas()
        objeto_analisis2.graficar_variables()

    def analisis_normalidad(self):
        print("\n=== Análisis de Normalidad ===")
        print("Población 1:")
        df_resultados = test_normalidad(self.pob1)
        print("Resultados de la prueba de normalidad:")
        print(df_resultados)
        print("\nPoblación 2:")
        df_resultados = test_normalidad(self.pob2)
        print("Resultados de la prueba de normalidad:")
        print(df_resultados)

    def docimas(self):
        docima = Docimas()
        print("\n=== Análisis de Docimas ===")
        
        while True:
            print("\n1-Docima respecto a medias y varianza poblacional") 
            print("\n2-Docima para comparar medias de dos poblaciones")
            print("\n3-Docimas para la proporcion poblacional")
            print("\n4-Docima para comparar la diferencia de proporciones")
            print("\n5-Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                mu_0 = float(input("Ingrese el valor de la media poblacional (mu_0): "))
                sigma = float(input("Ingrese el valor de la desviación estándar poblacional (sigma): "))
                sample = self.pob1["Nivel_de_Hemoglobina"].dropna().values
                z, p = docima.docima_media_varianza_conocida(sample, mu_0, sigma)
                print(f"Estadístico Z: {z}, p-valor: {p}")
            elif opcion == "2":
                mu_0 = float(input("Ingrese el valor de la media poblacional (mu_0): "))
                sample = self.pob1["Nivel_de_Hemoglobina"].dropna().values
                t_stat, p_value = docima.docima_media_varianza_desconocida(sample, mu_0)
                print(f"Estadístico T: {t_stat}, p-valor: {p_value}")
            elif opcion == "3":
                # Implementar lógica para proporciones
                pass
            elif opcion == "4":
                # Implementar lógica para comparar proporciones
                pass
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
            

    def pruebas(self):
        print("Análisis de General de Dependencias")
        print("Población 1:")
        #analizar_dependencias(self.pob1)
        print("Población 2:")
        #analizar_dependencias(self.pob2)

        print("Prueba de Dependencias")
        aux = input("¿Que población desea analizar? (1 o 2): ")
        if aux == "1":
            pob = self.pob1
        elif aux == "2":
            pob = self.pob2
        else:
            print("Opción no válida. Saliendo del análisis de dependencias.")
            return
        var_num = input("Ingrese la variable numérica: ")
        var_cat = input("Ingrese la variable categórica: ")
        bins = input("Ingrese los límites de los bins separados por comas: ").split(',')
        bins = [float(b) for b in bins]
        labels = input("Ingrese las etiquetas de los bins separados por comas: ").split(',')
        labels = [label.strip() for label in labels]
        prueba_independencia(pob, var_num, bins, labels, var_cat)

if __name__ == "__main__":
    menu = Menu()
    while True:
        continuar = menu.mostrar_menu()
        if continuar is False:
            break
        
    
