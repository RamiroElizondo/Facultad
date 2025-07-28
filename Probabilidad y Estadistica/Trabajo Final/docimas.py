import numpy as np
from scipy.stats import norm,chi2,t,f
from scipy.stats import t as t_dist
from scipy.stats import f as f_dist
import pandas as pd
import matplotlib.pyplot as plt

class Docimas:
    def __init__(self):
        pass

    def docima_varianza_conocida(self,mediaSample,n):
        """
        Docima respecto a medias y varianza poblacional conocida.
        """
        media = float(input("Ingrese la media a contrastar: "))
        varianzaPoblacional = float(input("Ingrese la varianza poblacional conocida: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        
        # Calcular el estadístico Z h0
        z = (mediaSample - media) / (np.sqrt(varianzaPoblacional) / np.sqrt(n))
        print(f"Z calculado: {z:.2f}")
        # Si mayor: H0: mu > media, hay que buscar en la tabla Z 1-alfa
        #self.graficar_docima('z', z, alfa, alternativa)
        self.graficar_z(z, alfa, alternativa, "Docima de media con varianza conocida")
        if alternativa == "mayor":
            z_critico = norm.ppf(1 - alfa).round(2)
            print(f"Z de tabla (1-alfa): {z_critico}")
            if z > z_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        # Si menor: H0: mu < media, hay que buscar en la tabla Z alfa
        elif alternativa == "menor":
            z_critico = norm.ppf(alfa).round(2)
            print(f"Z de tabla (alfa): {z_critico}")
            if z < z_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
                
        # Si diferente: H0: mu != media, hay que buscar en la tabla Z 1-alfa/2
        elif alternativa == "diferente":
            #redondear z criticas a dos decimales
            z_critico_der = norm.ppf(1 - alfa/2).round(2)
            z_critico_izq = norm.ppf(alfa/2).round(2)
            print(f"Z de tabla (1-alfa/2): {z_critico_der}, Z de tabla (alfa/2): {z_critico_izq}")
            if z < z_critico_izq or z > z_critico_der:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
        
        return z

    def docima_varianza_desconocida(self, mediaSample, varianzaSample,n):
       
        media = float(input("Ingrese la media a contrastar: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        #Calcular el estadístico t h0
        
        t_H0 = (mediaSample - media) / (np.sqrt(varianzaSample) / np.sqrt(n))
        # Si mayor: H0: mu > media, hay que buscar en la tabla t 1-alfa
        gl = n - 1  # grados de libertad

        print(f"t calculado: {t_H0:.2f}")
        #self.graficar_docima('t',t_H0, alfa, alternativa, gl)
        self.graficar_t(t_H0, alfa, alternativa, gl, "Docima de media con varianza desconocida")
        if alternativa == "mayor":
            t_critico = t_dist.ppf(1 - alfa, gl)
            print(f"T de tabla (1 - alfa): {t_critico:.2f}")
            if t_H0 > t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
        
        elif alternativa == "menor":
            t_critico = t_dist.ppf(alfa, gl)
            print(f"T de tabla (alfa): {t_critico:.2f}")
            if t_H0 < t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "diferente":
            t_critico = t_dist.ppf(1 - alfa / 2, gl)
            print(f"T de tabla (1 - alfa/2): ±{t_critico:.2f}")
            if abs(t_H0) > t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
        
        return t_H0

    def docima_media_varianza_desconocida(self, varianzaSample, n):
        varianza = float(input("Ingrese la varianza a contrastar: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        chi_cuadrado = ((n - 1) * varianzaSample) / varianza
        gl = n - 1
        print(f"Chi cuadrado calculado: {chi_cuadrado:.2f}")
        #Buscar en la tabla Chi Cuadrado
        #self.graficar_docima('chi', chi_cuadrado, alfa, alternativa, gl)
        self.graficar_chi(chi_cuadrado, alfa,alternativa,gl, "Docima de sigma cuadrado")
        if alternativa == "mayor":
            chi_critico = chi2.ppf(1 - alfa, gl)
            print(f"Chi cuadrado de tabla (1 - alfa): {chi_critico:.2f}")
            if chi_cuadrado > chi_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0.")
        elif alternativa == "menor":
            chi_critico = chi2.ppf(alfa, gl)
            print(f"Chi cuadrado de tabla (alfa): {chi_critico:.2f}")
            if chi_cuadrado < chi_critico:
               print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0.")
        elif alternativa == "diferente":
            chi_critico_izq = chi2.ppf(alfa / 2, gl)
            chi_critico_der = chi2.ppf(1 - alfa / 2, gl)
            print(f"Chi cuadrado de tabla (alfa/2): {chi_critico_izq:.2f}, Chi cuadrado de tabla (1 - alfa/2): {chi_critico_der:.2f}")
            if chi_cuadrado < chi_critico_izq or chi_cuadrado > chi_critico_der:
                print("Se rechaza H₀: hay evidencia de que la varianza es diferente a la hipotética.")
            else:
                print("No se rechaza H₀.")
        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
        
        return chi_cuadrado

    def docima_varianzas_conocidas_iguales(self, mediaSample1, mediaSample2, n1, n2):
        """
        Docima para comparar medias de dos poblaciones con varianzas conocidas iguales.
        """
        varianzaPoblacional = float(input("Ingrese la varianza poblacional conocida: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        # Calcular el estadístico Z
        z = (mediaSample1 - mediaSample2) / ((np.sqrt(varianzaPoblacional))*(np.sqrt(1/n1 + 1/n2)))
        print(f"Z calculado: {z:.2f}")
        #self.graficar_docima('z', z, alfa, alternativa)
        self.graficar_z(z, alfa, alternativa, "Docima de medias con varianzas conocidas iguales")
        if alternativa == "mayor":
            z_critico = norm.ppf(1 - alfa).round(2)
            print(f"Z de tabla (1-alfa): {z_critico}")
            if z > z_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "menor":
            z_critico = norm.ppf(alfa).round(2)
            print(f"Z de tabla (alfa): {z_critico}")
            if z < z_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "diferente":
            z_critico_der = norm.ppf(1 - alfa / 2).round(2)
            z_critico_izq = norm.ppf(alfa / 2).round(2)
            print(f"Z de tabla (1-alfa/2): {z_critico_der}, Z de tabla (alfa/2): {z_critico_izq}")
            if z < z_critico_izq or z > z_critico_der:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
       
        return z
    
    def docima_varianzas_conocidas_diferentes(self, mediaSample1, mediaSample2, varianzaPoblacional1, varianzaPoblacional2, n1, n2):
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        z = (mediaSample1 - mediaSample2) / np.sqrt(varianzaPoblacional1/n1 + varianzaPoblacional2/n2)
        print(f"Z calculado: {z:.2f}")
        #self.graficar_docima('z',z, alfa, alternativa)
        self.graficar_z(z, alfa, alternativa, "Docima de medias con varianzas conocidas diferentes")
        if alternativa == "mayor":
            z_critico = norm.ppf(1 - alfa).round(2)
            print(f"Z de tabla (1-alfa): {z_critico}")
            if z > z_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "menor":
            z_critico = norm.ppf(alfa).round(2)
            print(f"Z de tabla (alfa): {z_critico}")
            if z < z_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "diferente":
            z_critico_der = norm.ppf(1 - alfa / 2).round(2)
            z_critico_izq = norm.ppf(alfa / 2).round(2)
            print(f"Z de tabla (1-alfa/2): {z_critico_der}, Z de tabla (alfa/2): {z_critico_izq}")
            if z < z_critico_izq or z > z_critico_der:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
        
        return z
    
    def docima_varianza_desconocidas_iguales(self, mediaSample1, mediaSample2, varianzaSample1, varianzaSample2, tamano1, tamano2):
        
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        mayor,menor = 0,0
        n1,n2 = 0,0
        if varianzaSample1 > varianzaSample2:
            mayor = varianzaSample1
            menor = varianzaSample2
            n1 = tamano1
            n2 = tamano2
        else:
            mayor = varianzaSample2
            menor = varianzaSample1
            n1 = tamano2
            n2 = tamano1
        
        #calular F
        F = (mayor / menor).round(2)
        # hay que buscar el valor de F cuando tiene gl1 = n1 - 1 y gl2 = n2 - 1 y 1-alfa/2
        gl1 = n1 - 1
        gl2 = n2 - 1
        f_critico = f_dist.ppf(1 - alfa, gl1, gl2).round(2)
        print(f"F calculado: {F}, F crítico: {f_critico}")
        #self.graficar_docima('f', F, alfa, "diferente", gl1, gl2)
        self.graficar_f(F,alfa,"diferente", gl1, gl2, "Docima de varianzas con varianzas desconocidas iguales")
        if F > f_critico:
            print("Rechazamos la hipótesis nula H0")
            return
        print("No rechazamos la hipótesis nula H0")
        print("Construimos la docima para medias")
        print("Calculamos estadistico combinado")
        estadistico_combinado = ((n1-1)*varianzaSample1+(n2-1)*varianzaSample2)/(n1+n2-2)

        print(f"Estadístico combinado: {estadistico_combinado}")

        print("Construimos la variable pivotal t")

        t = (mediaSample1 - mediaSample2) / (np.sqrt(estadistico_combinado) * np.sqrt(1/n1 + 1/n2))

        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        gl = n1 + n2 - 2
        print(f"T calculado: {t:.2f}")
        #self.graficar_docima('t', t, alfa, alternativa, gl)
        self.graficar_t(t, alfa, alternativa, gl, "Docima de medias con varianzas desconocidas iguales")
        if alternativa == "mayor":
            t_critico = t_dist.ppf(1 - alfa, gl)
            print(f"T de tabla (1-alfa): {t_critico:.2f}")
            if t > t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "menor":
            t_critico = t_dist.ppf(alfa, gl)
            print(f"T de tabla (alfa): {t_critico:.2f}")
            if t < t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "diferente":
            t_critico = t_dist.ppf(1 - alfa / 2, gl)

            print(f"T de tabla (1-alfa/2): {t_critico:.2f}")
            if (t_critico * (-1)) > t or t > t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
        
        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
        
        return t
    
    def docima_varianza_desconocidas_diferentes(self, mediaSample1, mediaSample2, varianzaSample1, varianzaSample2, n1, n2):
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        # calculamos el t
        t = (mediaSample1 - mediaSample2) / np.sqrt(varianzaSample1/n1 + varianzaSample2/n2)

        gl = ((varianzaSample1/n1 + varianzaSample2/n2)**2 / ((varianzaSample1/n1)**2/(n1-1) + (varianzaSample2/n2)**2/(n2-1)))-2
        gl = int(gl)  # Convertir a entero para grados de libertad
        print(f"T calculado: {t:.2f}, Grados de libertad: {gl}")
        #self.graficar_docima('t', t, alfa, alternativa, gl)
        self.graficar_t(t, alfa, alternativa, gl, "Docima de medias con varianzas desconocidas diferentes")
        if alternativa == "mayor":
            t_critico = t_dist.ppf(1 - alfa, gl)
            print(f"T de tabla (1-alfa): {t_critico:.2f}")
            if t > t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "menor":
            t_critico = t_dist.ppf(alfa, gl)
            print(f"T de tabla (alfa): {t_critico:.2f}")
            if t < t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")

        elif alternativa == "diferente":
            t_critico = t_dist.ppf(1 - alfa / 2, gl)
            print(f"T de tabla (1-alfa/2): {t_critico:.2f}")
            if abs(t) > t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return None
        
        return t
   
    def docima_para_proporcion_poblacional(self,pob):
        variable = input("Ingrese la variable categórica para la docima: ")
        if variable not in pob.columns:
            print(f"La variable '{variable}' no se encuentra en la población seleccionada.")
            return None, None, None, None, None
        print(f"Variable seleccionada: {variable}")

        tamano_muestra = int(input("Ingrese el tamaño de la muestra: "))
        if tamano_muestra > len(pob):
            print("El tamaño de la muestra no puede ser mayor que el tamaño de la población.")
            return None, None, None, None, None
    
        sample = pob[variable].sample(n=tamano_muestra, random_state=1)

        exitos = float(input(f"Ingrese el número de éxitos para la variable '{variable}': "))
        exitos_muestra = exitos/ tamano_muestra
        exitospob = float(input(f"Ingrese el número de éxitos en la población para la variable '{variable} (20% -> 0.2)': "))

        z = (exitos_muestra - exitospob) / np.sqrt((exitospob*(1-exitospob))/tamano_muestra)

        
        print(f"Z calculado: {z:.2f}")
        alfa = float(input("Ingrese el nivel de significancia (alfa: 0.05): "))
        z_critico = norm.ppf(1 - alfa/2)
        print(f"Z crítico (1-alfa/2): {z_critico:.2f}")
        if abs(z) > z_critico:
            print("Rechazamos la hipótesis nula H0")
        else:
            print("No rechazamos la hipótesis nula H0")
        self.graficar_z(z, alfa, "diferenteProporciones", "Docima de proporción poblacional")

    def docima_diferencia_proporciones(self, pob1, pob2):
        variable = input("Ingrese la variable categórica para la docima: ")
        if variable not in pob1.columns or variable not in pob2.columns:
            print(f"La variable '{variable}' no se encuentra en las poblaciones seleccionadas.")
            return None, None, None, None, None
        print(f"Variable seleccionada: {variable}")

        tamano_muestra1 = int(input("Ingrese el tamaño de la muestra para la población 1: "))
        if tamano_muestra1 > len(pob1):
            print("El tamaño de la muestra no puede ser mayor que el tamaño de la población.")
            return None, None, None, None, None

        tamano_muestra2 = int(input("Ingrese el tamaño de la muestra para la población 2: "))
        if tamano_muestra2 > len(pob2):
            print("El tamaño de la muestra no puede ser mayor que el tamaño de la población.")
            return None, None, None, None, None

        sample1 = pob1[variable].sample(n=tamano_muestra1, random_state=1)
        sample2 = pob2[variable].sample(n=tamano_muestra2, random_state=1)

        exitos1 = float(input(f"Ingrese el número de éxitos para la variable '{variable}' en la población 1: "))
        exitos_muestra1 = exitos1 / tamano_muestra1

        exitos2 = float(input(f"Ingrese el número de éxitos para la variable '{variable}' en la población 2: "))
        exitos_muestra2 = exitos2 / tamano_muestra2

        exitospob1 = float(input(f"Ingrese el número de éxitos en la población 1 para la variable '{variable}' (20% -> 0.2): "))
        exitospob2 = float(input(f"Ingrese el número de éxitos en la población 2 para la variable '{variable}' (20% -> 0.2): "))

        p_raya = (exitos1 + exitos2) / (tamano_muestra1 + tamano_muestra2)

        numerador = (exitos_muestra1 - exitos_muestra2) - (exitospob1 - exitospob2) 
        denominador = np.sqrt(p_raya * (1 - p_raya) * (1/tamano_muestra1 + 1/tamano_muestra2))
        z = numerador / denominador
        print(f"Z calculado: {z:.2f}")
        alfa = float(input("Ingrese el nivel de significancia (alfa: 0.05): "))
        z_critico = norm.ppf(1 - alfa / 2)
        print(f"Z crítico (1-alfa/2): {z_critico:.2f}")
        if abs(z) > z_critico:
            print("Rechazamos la hipótesis nula H0")
        else:
            print("No rechazamos la hipótesis nula H0")
        self.graficar_z(z, alfa, "diferenteProporciones", "Docima de diferencia de proporciones")

    def p_valor(self,mediaSample, varianzaSample, n):
        print("Media Muestral:", mediaSample)
        print("Varianza Muestral:", varianzaSample)
        """
        Calcula el p-valor para una docima de media con varianza poblacional conocida.
        """
        media = float(input("Ingrese la media a contrastar: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        # Calcular el estadístico t
        print(mediaSample, "-", media, "/", np.sqrt(varianzaSample), "/", np.sqrt(n))
        t = (mediaSample - media) / (np.sqrt(varianzaSample) / np.sqrt(n))
        print(f"T calculado: {t:.2f}")
        # Calcular el p-valor
        gl = n - 1  # grados de libertad
        print(f"Grados de libertad: {gl}")

        if alternativa == "mayor":
            print("Calculando p-valor para la alternativa 'mayor'")
            # p-valor = p izq = P(T<t), hay que usar la tabla de t
            print("Calculando p-valor para la alternativa 'mayor")
            p_valor = 1 - t_dist.cdf(t, df=gl)

        elif alternativa == "menor":
            # p-valor = p der = P(T>t), hay que usar la tabla de t
            p_valor = t_dist.cdf(t, df=gl)
        elif alternativa == "diferente":
            print("Diferente",t_dist.cdf(t, df=gl))
            p_izq = t_dist.cdf(t, df=gl)
            p_der = 1 - t_dist.cdf(t, df=n-1)
            p_valor = 2 * min(p_izq, p_der)
        else:
            print("Alternativa no válida. Debe ser 'mayor', 'menor' o 'diferente'.")
            return
        if p_valor <= alfa:
            print("Rechazamos la hipótesis nula H0")
        else:
            print("No rechazamos la hipótesis nula H0")
        print(f"P-valor: {p_valor:.4f}")

    def graficar_chi_cuadrado(self,estadistico, gl, alfa, alternativa):
        x_min = max(0, chi2.ppf(0.001, gl))
        x_max = chi2.ppf(0.999, gl)
        x = np.linspace(x_min, x_max, 1000)
        y = chi2.pdf(x, gl)

        plt.plot(x, y, label=f'Distribución Chi-cuadrado (gl = {gl})')

        if alternativa == 'mayor':
            chi_critico = chi2.ppf(1 - alfa, gl)
            plt.fill_between(x, y, where=(x >= chi_critico), color='red', alpha=0.3, label='Zona de rechazo')
            plt.axvline(chi_critico, color='red', linestyle='--', label=f'chi crítico = {chi_critico:.2f}')
        elif alternativa == 'menor':
            chi_critico = chi2.ppf(alfa, gl)
            plt.fill_between(x, y, where=(x <= chi_critico), color='red', alpha=0.3, label='Zona de rechazo')
            plt.axvline(chi_critico, color='red', linestyle='--', label=f'chi crítico = {chi_critico:.2f}')
        elif alternativa == 'diferente':
            chi_crit_inf = chi2.ppf(alfa / 2, gl)
            chi_crit_sup = chi2.ppf(1 - alfa / 2, gl)
            plt.fill_between(x, y, where=(x <= chi_crit_inf) | (x >= chi_crit_sup), color='red', alpha=0.3, label='Zona de rechazo')
            plt.axvline(chi_crit_inf, color='red', linestyle='--', label=f'chi crítico inf = {chi_crit_inf:.2f}')
            plt.axvline(chi_crit_sup, color='red', linestyle='--', label=f'chi crítico sup = {chi_crit_sup:.2f}')

        plt.axvline(estadistico, color='blue', label=f'Estadístico = {estadistico:.2f}')
        plt.title('Prueba de Hipótesis')
        plt.xlabel('Estadístico')
        plt.ylabel('Densidad')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def graficar_docima(self,estadistico, valor_calculado, alfa, alternativa, gl1=None, gl2=None):
        """
        Grafica la región de rechazo y el valor observado para una prueba de hipótesis.

        Parámetros:
            estadistico: 'z', 't', 'chi' o 'f'
            valor_calculado: valor del estadístico observado
            alfa: nivel de significancia
            alternativa: 'mayor', 'menor' o 'diferente'
            gl1: grados de libertad (para t, chi, f)
            gl2: grados de libertad del denominador (sólo para F)
        """
        x = None
        dist = None
        etiqueta = None

        if estadistico == 'z':
            x = np.linspace(-4, 4, 1000)
            dist = norm(0, 1)
            etiqueta = 'Distribución Normal (Z)'
        elif estadistico == 't':
            if gl1 is None:
                raise ValueError("Se requieren grados de libertad (gl1) para t")
            x = np.linspace(-5, 5, 1000)
            dist = t(df=gl1)
            etiqueta = f'Distribución t (gl = {gl1})'
        elif estadistico == 'chi':
            if gl1 is None:
                raise ValueError("Se requieren grados de libertad (gl1) para Chi-cuadrado")
            x = np.linspace(0.001, chi2.ppf(0.999, df=gl1), 1000)
            dist = chi2(df=gl1)
            etiqueta = f'Distribución Chi-cuadrado (gl = {gl1})'
        elif estadistico == 'f':
            if gl1 is None or gl2 is None:
                raise ValueError("Se requieren gl1 y gl2 para F")
            x = np.linspace(0.001, f_dist.ppf(0.999, dfn=gl1, dfd=gl2), 1000)
            dist = f(dfn=gl1, dfd=gl2)
            etiqueta = f'Distribución F (gl1 = {gl1}, gl2 = {gl2})'
        else:
            raise ValueError("Estadístico no válido. Usa 'z', 't', 'chi' o 'f'.")

        y = dist.pdf(x)

        # Graficar curva
        plt.figure(figsize=(9, 5))
        plt.plot(x, y, label=etiqueta)
        plt.title('Prueba de Hipótesis')
        plt.xlabel('Estadístico')
        plt.ylabel('Densidad')

        # Zonas de rechazo
        if alternativa == 'mayor':
            zc = dist.ppf(1 - alfa)
            plt.fill_between(x, 0, y, where=(x > zc), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(zc, color='red', linestyle='--', label=f'{estadistico} crítico = {zc:.2f}')
        elif alternativa == 'menor':
            zc = dist.ppf(alfa)
            plt.fill_between(x, 0, y, where=(x < zc), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(zc, color='red', linestyle='--', label=f'{estadistico} crítico = {zc:.2f}')
        elif alternativa == 'diferente':
            zc_izq = dist.ppf(alfa / 2)
            zc_der = dist.ppf(1 - alfa / 2)
            plt.fill_between(x, 0, y, where=(x < zc_izq), color='red', alpha=0.4)
            plt.fill_between(x, 0, y, where=(x > zc_der), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(zc_izq, color='red', linestyle='--', label=f'{estadistico} crítico izq = {zc_izq:.2f}')
            plt.axvline(zc_der, color='red', linestyle='--', label=f'{estadistico} crítico der = {zc_der:.2f}')
        else:
            raise ValueError("Alternativa no válida. Usa 'mayor', 'menor' o 'diferente'.")

        # Línea del valor calculado
        plt.axvline(valor_calculado, color='blue', linestyle='-', label=f'Estadístico = {valor_calculado:.2f}')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def graficar_z(self, valor_calculado, alfa, alternativa, docima):
        """
        Grafica la región de rechazo y el valor observado para una prueba Z.
        """
        x = np.linspace(-4, 4, 1000)
        dist = norm(0, 1)
        y = dist.pdf(x)
        
        # Graficar curva
        plt.figure(figsize=(9, 5))
        plt.plot(x, y, label='Distribución Normal (Z)')
        plt.title(docima)
        plt.xlabel('Estadístico Z')
        plt.ylabel('Densidad')

        # Zonas de rechazo
        if alternativa == 'mayor':
            z_critico = dist.ppf(1 - alfa)
            plt.fill_between(x, 0, y, where=(x > z_critico), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(z_critico, color='red', linestyle='--', label=f'Z crítico = {z_critico:.2f}')
        elif alternativa == 'menor':
            z_critico = dist.ppf(alfa)
            plt.fill_between(x, 0, y, where=(x < z_critico), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(z_critico, color='red', linestyle='--', label=f'Z crítico = {z_critico:.2f}')
        elif alternativa == 'diferente':
            z_critico_izq = dist.ppf(alfa / 2)
            z_critico_der = dist.ppf(1 - alfa / 2)
            plt.fill_between(x, 0, y, where=(x < z_critico_izq), color='red', alpha=0.4)
            plt.fill_between(x, 0, y, where=(x > z_critico_der), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(z_critico_izq, color='red', linestyle='--', label=f'Z crítico izq = {z_critico_izq:.2f}')
            plt.axvline(z_critico_der, color='red', linestyle='--', label=f'Z crítico der = {z_critico_der:.2f}')
        elif alternativa == 'diferenteProporciones':
            z_critico_izq = dist.ppf(1 - alfa / 2)*(-1)
            z_critico_der = dist.ppf(1 - alfa / 2)
            plt.fill_between(x, 0, y, where=(x < z_critico_izq), color='red', alpha=0.4)
            plt.fill_between(x, 0, y, where=(x > z_critico_der), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(z_critico_izq, color='red', linestyle='--', label=f'Z crítico izq = {z_critico_izq:.2f}')
            plt.axvline(z_critico_der, color='red', linestyle='--', label=f'Z crítico der = {z_critico_der:.2f}')
        # Línea del valor calculado
        plt.axvline(valor_calculado, color='blue', linestyle='-', label=f'Z calculado = {valor_calculado:.2f}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def graficar_t(self, valor_calculado, alfa, alternativa, gl, docima):
        """
        Grafica la región de rechazo y el valor observado para una prueba t.
        """
        x = np.linspace(-5, 5, 1000)
        dist = t(df=gl)
        y = dist.pdf(x)
        
        # Graficar curva
        plt.figure(figsize=(9, 5))
        plt.plot(x, y, label=f'Distribución t (gl = {gl})')
        plt.title(docima)
        plt.xlabel('Estadístico t')
        plt.ylabel('Densidad')

        # Zonas de rechazo
        if alternativa == 'mayor':
            t_critico = dist.ppf(1 - alfa)
            plt.fill_between(x, 0, y, where=(x > t_critico), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(t_critico, color='red', linestyle='--', label=f't crítico = {t_critico:.2f}')
        elif alternativa == 'menor':
            t_critico = dist.ppf(alfa)
            plt.fill_between(x, 0, y, where=(x < t_critico), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(t_critico, color='red', linestyle='--', label=f't crítico = {t_critico:.2f}')
        elif alternativa == 'diferente':
            t_critico_izq = dist.ppf(1 - alfa / 2) * (-1)
            t_critico_der = dist.ppf(1 - alfa / 2)
            plt.fill_between(x, 0, y, where=(x < t_critico_izq), color='red', alpha=0.4)
            plt.fill_between(x, 0, y, where=(x > t_critico_der), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(t_critico_izq, color='red', linestyle='--', label=f't crítico izq = {t_critico_izq:.2f}')
            plt.axvline(t_critico_der, color='red', linestyle='--', label=f't crítico der = {t_critico_der:.2f}')

        # Línea del valor calculado
        plt.axvline(valor_calculado, color='blue', linestyle='-', label=f't calculado = {valor_calculado:.2f}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def graficar_chi(self, valor_calculado, alfa, alternativa, gl, docima):
        """
        Grafica la región de rechazo y el valor observado para una prueba Chi-cuadrado.
        """
        x = np.linspace(0.001, chi2.ppf(0.999, df=gl), 1000)
        dist = chi2(df=gl)
        y = dist.pdf(x)
        
        # Graficar curva
        plt.figure(figsize=(9, 5))
        plt.plot(x, y, label=f'Distribución Chi-cuadrado (gl = {gl})')
        plt.title(docima)
        plt.xlabel('Estadístico Chi-cuadrado')
        plt.ylabel('Densidad')

        # Zonas de rechazo
        if alternativa == 'mayor':
            chi_critico = dist.ppf(1 - alfa)
            plt.fill_between(x, 0, y, where=(x > chi_critico), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(chi_critico, color='red', linestyle='--', label=f'Chi crítico = {chi_critico:.2f}')
        elif alternativa == 'menor':
            chi_critico = dist.ppf(alfa)
            plt.fill_between(x, 0, y, where=(x < chi_critico), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(chi_critico, color='red', linestyle='--', label=f'Chi crítico = {chi_critico:.2f}')
        elif alternativa == 'diferente':
            chi_critico_izq = dist.ppf(alfa / 2)
            chi_critico_der = dist.ppf(1 - alfa / 2)
            plt.fill_between(x, 0, y, where=(x < chi_critico_izq), color='red', alpha=0.4)
            plt.fill_between(x, 0, y, where=(x > chi_critico_der), color='red', alpha=0.4, label='Zona de rechazo')
            plt.axvline(chi_critico_izq, color='red', linestyle='--', label=f'Chi crítico izq = {chi_critico_izq:.2f}')
            plt.axvline(chi_critico_der, color='red', linestyle='--', label=f'Chi crítico der = {chi_critico_der:.2f}')

        # Línea del valor calculado
        plt.axvline(valor_calculado, color='blue', linestyle='-', label=f'Chi calculado = {valor_calculado:.2f}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def graficar_f(self, valor_calculado, alfa, alternativa, gl1, gl2, docima):
        """
        Grafica la región de rechazo y el valor observado para una prueba F.
        """
        x = np.linspace(0.001, f_dist.ppf(0.999, dfn=gl1, dfd=gl2), 1000)
        dist = f(dfn=gl1, dfd=gl2)
        y = dist.pdf(x)
        
        # Graficar curva
        plt.figure(figsize=(9, 5))
        plt.plot(x, y, label=f'Distribución F (gl1 = {gl1}, gl2 = {gl2})')
        plt.title(docima)
        plt.xlabel('Estadístico F')
        plt.ylabel('Densidad')

        # Zonas de rechazo

        f_critico = dist.ppf(1 - alfa / 2)
        plt.fill_between(x, 0, y, where=(x > f_critico), color='red', alpha=0.4, label='Zona de rechazo')
        plt.axvline(f_critico, color='red', linestyle='--', label=f'F crítico = {f_critico:.2f}')

        # Línea del valor calculado
        plt.axvline(valor_calculado, color='blue', linestyle='-', label=f'F calculado = {valor_calculado:.2f}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()