import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew, kurtosis, mode

class AnalisisExploratorio:
    """
    Clase para realizar análisis exploratorio de datos.
    Incluye carga de datos, estadísticas descriptivas y visualización.
    """
    
    def __init__(self, data):
        self.__data = data
    
    def menu(self):
        """
        Muestra el menú de opciones para el análisis exploratorio.
        """
        opcion = ''
        while opcion != '5':
            print("\n===== MENÚ ANÁLISIS EXPLORATORIO =====")
            print("1. Mostrar información del dataset")
            print("2. Ver Descripciones Generales")
            print("3. Visualizar variables")
            print("4. Coeficiente de correlación")
            print("5. Salir")

            opcion = input("Seleccione una opción (5 para salir): ")
            if opcion == '1':
                self.mostrar_info()
            elif opcion == '2':
                self.descriptivas()
            elif opcion == '3':
                self.histograma('IMC')
            elif opcion == '4':
                columna1 = input("Ingrese el nombre de la primera columna: ")
                columna2 = input("Ingrese el nombre de la segunda columna: ")
                self.coef_Correlacion(columna1, columna2)
            elif opcion == '5':
                print("Saliendo del menú de análisis exploratorio...")
    
    def mostrar_info(self):
        """
        Muestra información general del dataset (dimensiones, tipos de datos, valores nulos).
        """
        print("\nInformación del dataset:")
        print(self.__data.info())
        print("\nPrimeras filas del dataset:")
        print(self.__data.head())
    
    def menu_variables(self):
        """
        Muestra un menú con las variables relevantes y permite seleccionar una.
        """
        variables = [
            "Edad", 
            "Conteo_de_Globulos_blancos", 
            "Conteo_de_Globulos_rojos",
            "Conteo_de_Plaquetas", 
            "Nivel_de_Hemoglobina", 
            "Blastos_de_Médula_Osea", 
            "IMC"
        ]
        print("\n---- Variables Disponibles ----")
        for i, var in enumerate(variables, start=1):
            print(f"{i}. {var}")
        print("-------------------------------")
        try:
            opcion = int(input("Seleccione el número de la variable a analizar: "))
            if 1 <= opcion <= len(variables):
                return variables[opcion - 1]
            else:
                print("Opción inválida. Intente nuevamente.")
                return self.menu_variables()
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
            return self.menu_variables()
        
    def descriptivas(self):
        columna = self.menu_variables()
        if columna not in self.__data.columns:
            print("Error: La columna no existe en el dataset.")
            return
        """
        Calcula y muestra estadísticas descriptivas de la variable seleccionada.
        :param columna: str - Nombre de la columna numérica a analizar.
        """
        
        datos = self.__data[columna].dropna()
        estadisticas = {
            "Media": datos.mean(),
            "Mediana": datos.median(),
            "Moda/s":datos.mode().values.tolist(),
            "Varianza": datos.var(),
            "Desviación estándar": datos.std(),
            "Coef. de variación": datos.std() / datos.mean() if datos.mean() != 0 else 0,
            "Máximo": datos.max(),
            "Mínimo": datos.min(),
            "Rango": datos.max() - datos.min(),
            "Coef. de asimetría": skew(datos),
            "Coef. de curtosis": kurtosis(datos),
            "P - 0.25": datos.quantile(0.25),
            "P - 0.50": datos.quantile(0.50),
            "P - 0.75": datos.quantile(0.75)
        }
        
        print("\nEstadísticas descriptivas para", columna)
        for clave, valor in estadisticas.items():
            print(f"{clave}: {valor}")
    
    def histograma(self, columna):
        """
        Genera histogramas de las variables numéricas más relevantes.
        """
        variables_relevantes = [
            "Conteo_de_Globulos_blancos", "Conteo_de_Globulos_rojos",
            "Conteo_de_Plaquetas", "Nivel_de_Hemoglobina", "Blastos_de_Médula_Osea", "IMC"
        ]
        for columna in variables_relevantes:
            plt.figure(figsize=(8, 5))
            sns.histplot(self.__data[columna], kde=True, bins=30)
            plt.title(f'Histograma de {columna}')
            plt.xlabel(columna)
            plt.ylabel('Frecuencia')
            plt.show()
    
    def correlacion(self):
        """
        Calcula y visualiza la matriz de correlación entre variables numéricas relevantes.
        """
        variables_numericas = [
            "Edad", "Conteo_de_Globulos_blancos", "Conteo_de_Globulos_rojos",
            "Conteo_de_Plaquetas", "Nivel_de_Hemoglobina", "Blastos_de_Médula_Osea", "IMC"
        ]
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.__data[variables_numericas].corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Matriz de correlación')
        plt.show()

    def coef_Correlacion(self, columna1, columna2):
        print("------------------------")
        print("Coeficiente de correlación de las variables Bodyfat y Weight")
        # Coeficiente de correlación
        print('Coeficiente de correlacion: ', self.__data.Conteo_de_Globulos_rojos.corr(self.__data.Nivel_de_Hemoglobina))
        print("------------------------")

