import pandas as pd
from pathlib import Path
from dependencias import analizar_dependencias, prueba_dependencias, prueba_independencia
from analisis_exploratorio import Analisis_exploratorio
from normal import test_normalidad
from docimas import Docimas
import os

class Menu:
    def __init__(self):
        #self.dividir_dataset()
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

    def dividir_dataset(self):
        # Cargar el dataset
        df = pd.read_csv("biased_leukemia_dataset.csv")

        # Filtrar pacientes por país
        poblacion_1 = df[df["País"] == "India"].copy()
        poblacion_2 = df[df["País"] == "USA"].copy()

        print(f"Población 1 (India): {len(poblacion_1)} registros")
        print(f"Población 2 (USA): {len(poblacion_2)} registros")

        # Guardar en archivos CSV
        poblacion_1.to_csv("poblacionINDIA.csv", index=False)
        poblacion_2.to_csv("poblacionUSA.csv", index=False)

    def cargar_datasets(self):
        # Ruta del dataset original
        # Una vez dividido, cargamos las poblaciones
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        RUTA_CSV_ORIGINAL = os.path.join(BASE_DIR, "biased_leukemia_dataset.csv")
        RUTA_CSV_POB1 = os.path.join(BASE_DIR, "poblacionINDIA.csv")
        RUTA_CSV_POB2 = os.path.join(BASE_DIR, "poblacionUSA.csv")

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
        #objeto_analisis1.guardar_graficos()

        print("\n=== Análisis de la Población 2 ===")
        objeto_analisis2 = Analisis_exploratorio(id=2,data=self.pob2)
        objeto_analisis2.estadisticas_descriptivas()
        objeto_analisis2.graficar_variables()
        #objeto_analisis2.guardar_graficos()

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

    def creacion_muestra(self, pob, n=5000, condicion=None):
        variable = input("Ingrese la variable numérica para la docima: ")
        if variable not in pob.columns:
            print(f"La variable '{variable}' no se encuentra en la población seleccionada.")
            return None, None, None, None, None
        print(f"Variable seleccionada: {variable}")
        if condicion != None:
            #La condicion puede ser: pacientes menores de 30 años, pacientes mayores a 60 años, pacientes mujeres,
            if condicion == "menores_30":
                pob_filtrada = pob[pob["Edad"] < 30]
            elif condicion == "mayores_60":
                pob_filtrada = pob[pob["Edad"] > 60]
            elif condicion == "mujeres":
                pob_filtrada = pob[pob["Género"] == "Female"]
            elif condicion == "estado_positivo":
                pob_filtrada = pob[pob["Estado_de_Leucemia"] == "Positive"]
            sample = pob_filtrada.loc[pob_filtrada["Género"] == "Female", variable]
            mediaSample = sample.mean()
            varianzaSample = sample.var(ddof=1)

            mediaPoblacional = pob[variable].mean()
            varianzaPoblacional = pob[variable].var(ddof=1)
            return sample, mediaSample, varianzaSample, mediaPoblacional, varianzaPoblacional
        else: 
            sample = pob[variable].dropna().sample(n, random_state=42)
            mediaSample = sample.mean()
            varianzaSample = sample.var(ddof=1)

            mediaPoblacional = pob[variable].mean()
            varianzaPoblacional = pob[variable].var(ddof=1)
            return sample, mediaSample, varianzaSample, mediaPoblacional, varianzaPoblacional

    """ def creacion_muestra(self, pob, n, condicion=None):
        variable = input("Ingrese la variable numérica para la docima: ")
        if variable not in pob.columns:
            print(f"La variable '{variable}' no se encuentra en la población seleccionada.")
            return None, None, None, None, None
        print(f"Variable seleccionada: {variable}")
        if condicion != None:
            #La condicion puede ser: pacientes menores de 30 años, pacientes mayores a 60 años, pacientes mujeres,
            if condicion == "menores_30":
                pob = pob[pob["Edad"] < 30]
            elif condicion == "mayores_60":
                pob = pob[pob["Edad"] > 60]
            elif condicion == "mujeres":
                pob = pob[pob["Género"] == "Female"]
        sample = pob[variable].dropna().sample(n, random_state=42)
        mediaSample = sample.mean()
        varianzaSample = sample.var(ddof=1)

        mediaPoblacional = pob[variable].mean()
        varianzaPoblacional = pob[variable].var(ddof=1)
        return sample, mediaSample, varianzaSample, mediaPoblacional, varianzaPoblacional"""

    def docimas(self):
        docima = Docimas()
        print("\n=== Análisis de Docimas ===")
        
        while True:
            print("\nSeleccione el tipo de docima que desea realizar:")
            print("1-Docima respecto a medias y varianza poblacional") 
            print("2-Docima para comparar medias de dos poblaciones")
            print("3-Docimas para la proporcion poblacional")
            print("4-Docima para comparar la diferencia de proporciones")
            print("5-P-valor")
            print("6-Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "6":
                print("Saliendo del análisis de docimas...")
                break
            if opcion == "1":
                aux = input("¿Que población: (1 o 2)? ")
                pob = None
                if aux == "1":
                    pob = self.pob1.copy()
                    print("Población 1 seleccionada.")
                elif aux == "2":
                    pob = self.pob2.copy()
                    print("Población 2 seleccionada.")
                else:
                    print("Opción no válida. Intente nuevamente.")
                    continue
                print("\n==== Docima respecto a medias y varianza poblacional ====\n")
                print("-----Docima para mu cuando sigma cuadrado es conocido")
                n = int(input("Ingrese el tamaño de la muestra: "))
               
                sample, mediaSample, varianzaSample, mediaPoblacional, varianzaPoblacional = self.creacion_muestra(pob,n)
                if sample is None:
                    print("Muestra no válida. Intente nuevamente.")
                    continue
                valor = docima.docima_varianza_conocida(mediaSample,n)
                if valor is None:
                    continue

                print("\n-----Docima para mu cuando sigma cuadrado es desconocido")
                n = int(input("Ingrese el tamaño de la muestra: "))
                sample, mediaSample, varianzaSample, mediaPoblacional, varianzaPoblacional = self.creacion_muestra(pob,n)
                if sample is None:
                    continue
                valor = docima.docima_varianza_desconocida(mediaSample, varianzaSample,n)
                if valor is None:
                    continue
                
                print("\n------Docima para sigma cuadrado")
                n = int(input("Ingrese el tamaño de la muestra: "))
                sample, mediaSample, varianzaSample, mediaPoblacional, varianzaPoblacional = self.creacion_muestra(pob,n)
                if sample is None:
                    continue
                valor=docima.docima_media_varianza_desconocida(varianzaSample,n)
                if valor is None:
                    continue
            
            elif opcion == "2":
                print("\n==== Docima para comparar medias de dos poblaciones ====\n")
                #Muestra 1
                """print("-----Docima para varianzas conocidas iguales")
                condicion = input("Condicion de la muestra: ")
                print("Población 1:")
                sample1, mediaSample1, varianzaSample1, mediaPoblacional1, varianzaPoblacional1 = self.creacion_muestra(self.pob1, condicion=condicion)
                print("Población 2:")
                sample2, mediaSample2, varianzaSample2, mediaPoblacional2, varianzaPoblacional2 = self.creacion_muestra(self.pob2, condicion=condicion)
                if sample1 is None or sample2 is None:
                    continue
                
                valor = docima.docima_varianzas_conocidas_iguales(mediaSample1, mediaSample2, len(sample1), len(sample2))
                if valor is None:
                    continue

                print("\n-----Docima para varianzas conocidas diferentes")
                condicion = input("Condicion de la muestra: ")
                print("Población 1:")
                sample1, mediaSample1, varianzaSample1, mediaPoblacional1, varianzaPoblacional1 = self.creacion_muestra(self.pob1, condicion=condicion)
                print("Población 2:")
                sample2, mediaSample2, varianzaSample2, mediaPoblacional2, varianzaPoblacional2 = self.creacion_muestra(self.pob2, condicion=condicion)
                
                valor = docima.docima_varianzas_conocidas_diferentes(mediaSample1, mediaSample2, varianzaPoblacional1,varianzaPoblacional2, len(sample1), len(sample2))
                if valor is None:
                    continue"""

                print("\n-----Docima para varianzas desconocidas iguales")
                condicion = input("Condicion de la muestra: ")
                print("Población 1:")
                sample1, mediaSample1, varianzaSample1, mediaPoblacional1, varianzaPoblacional1 = self.creacion_muestra(self.pob1, condicion=condicion)
                print("Población 2:")
                sample2, mediaSample2, varianzaSample2, mediaPoblacional2, varianzaPoblacional2 = self.creacion_muestra(self.pob2, condicion=condicion)

                valor = docima.docima_varianza_desconocidas_iguales(mediaSample1,mediaSample2,varianzaSample1, varianzaSample2, len(sample1), len(sample2))
                if valor is None:
                    continue    
                print("\n-----Docima para varianzas desconocidas diferentes")
                print("Población 1:")
                sample1, mediaSample1, varianzaSample1, mediaPoblacional1, varianzaPoblacional1 = self.creacion_muestra(self.pob1, condicion=condicion)
                print("Población 2:")
                sample2, mediaSample2, varianzaSample2, mediaPoblacional2, varianzaPoblacional2 = self.creacion_muestra(self.pob2, condicion=condicion)
                valor = docima.docima_varianza_desconocidas_diferentes(mediaSample1,mediaSample2, varianzaSample1, varianzaSample2, len(sample1), len(sample2))
                if valor is None:
                    continue
            elif opcion == "3":
                aux = input("¿Que población: (1 o 2)? ")
                pob = None
                if aux == "1":
                    pob = self.pob1.copy()
                    print("Población 1 seleccionada.")
                elif aux == "2":
                    pob = self.pob2.copy()
                    print("Población 2 seleccionada.")
                else:
                    print("Opción no válida. Intente nuevamente.")
                    continue
                docima.docima_para_proporcion_poblacional(pob)
            elif opcion == "4":
                docima.docima_diferencia_proporciones(self.pob1, self.pob2)
            elif opcion == "5":
                condicion = input("Condicion de la muestra: ")

                aux = input("¿Que población: (1 o 2)? ")
                pob = None
                if aux == "1":
                    pob = self.pob1.copy()
                    print("Población 1 seleccionada.")
                elif aux == "2":
                    pob = self.pob2.copy()
                    print("Población 2 seleccionada.")
                else:
                    print("Opción no válida. Intente nuevamente.")
                    continue
                
                # crear muestra aca
                variable = input("Ingrese la variable numérica para el p-valor: ")
                if variable not in pob.columns:
                    print(f"La variable '{variable}' no se encuentra en la población seleccionada.")
                    continue
                print(f"Variable seleccionada: {variable}")
                condicion = input("Ingrese la condicion de la muestra (menores_30, mayores_60, mujeres, estado_positivo): ")
                pob_filtrada = pob.loc[pob["Estado_de_Leucemia"] == "Positive", variable]
                
                n = int(input("Ingrese el tamaño de la muestra: "))
                sample = pob[variable].dropna().sample(n, random_state=42)
                mediaSample = sample.mean()
                varianzaSample = sample.var(ddof=1)
                docima.p_valor(mediaSample, varianzaSample, len(sample))
            else:
                print("Opción no válida. Intente nuevamente.")
                continue
    def pruebas(self):
        """print("Análisis de General de Dependencias")
        print("Población 1:")
        analizar_dependencias(self.pob1)
        print("Población 2:")
        analizar_dependencias(self.pob2)"""

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
        #print(pob[var_num].describe())
        #print(pob[var_num].unique())
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
        
    
