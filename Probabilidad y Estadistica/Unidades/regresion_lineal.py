import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class RegresionLineal:
    """
    Clase para realizar regresión lineal siguiendo la teoría del apunte.
    Se basa en el modelo: Y = α + βX + ε, donde ε ~ N(0, σ²).
    """
    
    def __init__(self, datos, variable_x, variable_y):
        """
        Inicializa la regresión lineal.
        :param datos: DataFrame con los datos.
        :param variable_x: Nombre de la variable independiente (X).
        :param variable_y: Nombre de la variable dependiente (Y).
        """
        self.datos = datos.dropna(subset=[variable_x, variable_y])  # Eliminar valores nulos
        self.variable_x = variable_x
        self.variable_y = variable_y
        self.modelo = None
        self.predicciones = None
        self.r2 = None
        self.mse = None
        self.alpha = None
        self.beta = None
    
    def menu(self):
        """
        Muestra el menú de opciones para la regresión lineal.
        """
        opcion = ''
        while opcion != '5':
            print("\n===== MENÚ REGRESIÓN LINEAL =====")
            print("1. Estimar parámetros (mínimos cuadrados)")
            print("2. Entrenar modelo (scikit-learn)")
            print("3. Graficar regresión")
            print("4. Analizar residuales")
            print("5. Mostrar resultados")
            print("6. Salir")
            
            opcion = input("Seleccione una opción (6 para salir): ")
            if opcion == '1':
                self.estimar_parametros()
            elif opcion == '2':
                self.entrenar_modelo()
            elif opcion == '3':
                self.graficar_regresion()
            elif opcion == '4':
                self.analizar_residuales()
            elif opcion == '5':
                self.mostrar_resultados()
            elif opcion == '6':
                print("Saliendo del menú de regresión lineal...")

    def estimar_parametros(self):
        """
        Calcula los coeficientes de regresión (mínimos cuadrados).
        """
        X = self.datos[self.variable_x].values
        y = self.datos[self.variable_y].values
        
        # Cálculo de parámetros usando fórmulas de mínimos cuadrados
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        self.beta = np.sum((X - X_mean) * (y - y_mean)) / np.sum((X - X_mean) ** 2)
        self.alpha = y_mean - self.beta * X_mean
        
        print(f"Parámetros estimados: α = {self.alpha:.4f}, β = {self.beta:.4f}")
    
    def entrenar_modelo(self):
        """
        Entrena el modelo de regresión lineal con scikit-learn.
        """
        X = self.datos[[self.variable_x]].values.reshape(-1, 1)
        y = self.datos[self.variable_y].values
        
        self.modelo = LinearRegression()
        self.modelo.fit(X, y)
        self.predicciones = self.modelo.predict(X)
        
        # Evaluación del modelo
        self.r2 = r2_score(y, self.predicciones)
        self.mse = mean_squared_error(y, self.predicciones)
    
    def graficar_regresion(self):
        """
        Genera un gráfico de dispersión con la línea de regresión.
        """
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=self.datos[self.variable_x], y=self.datos[self.variable_y], label="Datos Reales")
        plt.plot(self.datos[self.variable_x], self.predicciones, color='red', label='Línea de Regresión')
        plt.xlabel(self.variable_x)
        plt.ylabel(self.variable_y)
        plt.title(f'Regresión Lineal: {self.variable_x} vs {self.variable_y}')
        plt.legend()
        plt.show()
    
    def analizar_residuales(self):
        """
        Grafica los residuales del modelo para validar los supuestos.
        """
        residuales = self.datos[self.variable_y] - self.predicciones
        
        plt.figure(figsize=(8, 5))
        sns.histplot(residuales, kde=True, bins=30)
        plt.axvline(0, color='red', linestyle='dashed')
        plt.title('Distribución de los Residuales')
        plt.xlabel('Residual')
        plt.ylabel('Frecuencia')
        plt.show()
    
    def mostrar_resultados(self):
        """
        Imprime los resultados de la regresión lineal.
        """
        print(f"Coeficiente de regresión (β): {self.modelo.coef_[0]:.4f}")
        print(f"Intercepto (α): {self.modelo.intercept_:.4f}")
        print(f"Coeficiente de determinación (R²): {self.r2:.4f}")
        print(f"Error cuadrático medio (MSE): {self.mse:.4f}")
