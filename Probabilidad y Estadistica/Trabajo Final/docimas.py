import numpy as np
from scipy.stats import ttest_1samp, norm, chi2
from scipy.stats import t as t_dist
from scipy.stats import f as f_dist

class Docimas:
    def __init__(self):
        pass

    def docima_varianza_conocida(self,mediaSample, varianzaPoblacional,n):
        """
        Docima respecto a medias y varianza poblacional conocida.
        """
        media = float(input("Ingrese la media a contrastar: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        
        # Calcular el estadístico Z h0
        z = (mediaSample - media) / (np.sqrt(varianzaPoblacional) / np.sqrt(n))

        # Si mayor: H0: mu > media, hay que buscar en la tabla Z 1-alfa
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

    def docima_varianza_desconocida(self, mediaSample, varianzaSample,n):
       
        media = float(input("Ingrese la media a contrastar: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        #Calcular el estadístico t h0
        
        t_H0 = (mediaSample - media) / (np.sqrt(varianzaSample) / np.sqrt(n))
        # Si mayor: H0: mu > media, hay que buscar en la tabla t 1-alfa
        gl = n - 1  # grados de libertad

        print(f"t calculado: {t_H0:.2f}")
        
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

    def docima_media_varianza_desconocida(self, varianzaSample, n):
        varianza = float(input("Ingrese la varianza a contrastar: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))
        chi_cuadrado = (n - 1) * varianzaSample / varianza
        gl = n - 1
        print(f"Chi cuadrado calculado: {chi_cuadrado:.2f}")
        #Buscar en la tabla Chi Cuadrado
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

    def docima_varianzas_conocidas_iguales(self, mediaSample1, mediaSample2, n1, n2):
        """
        Docima para comparar medias de dos poblaciones con varianzas conocidas iguales.
        """
        varianzaPoblacional = float(input("Ingrese la varianza poblacional conocida: "))
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        # Calcular el estadístico Z
        z = (mediaSample1 - mediaSample2) / (np.sqrt(varianzaPoblacional))*(np.sqrt(1/n1 + 1/n2))

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

    def docima_varianzas_conocidas_diferentes(self, mediaSample1, mediaSample2, varianzaPoblacional1, varianzaPoblacional2, n1, n2):
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        z = (mediaSample1 - mediaSample2) / np.sqrt(varianzaPoblacional1/n1 + varianzaPoblacional2/n2)
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

    def docima_varianza_desconocidas_iguales(self, mediaSample1, mediaSample2, varianzaSample1, varianzaSample2, n1, n2):
        
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        mayor,menor = 0
        if varianzaSample1 > varianzaSample2:
            mayor = varianzaSample1
            menor = varianzaSample2
        else:
            mayor = varianzaSample2
            menor = varianzaSample1
        
        #calular F
        F = (mayor / menor).round(2)
        # hay que buscar el valor de F cuando tiene gl1 = n1 - 1 y gl2 = n2 - 1 y 1-alfa/2
        gl1 = n1 - 1
        gl2 = n2 - 1
        f_critico = f_dist.ppf(1 - alfa, gl1, gl2).round(2)
        print(f"F calculado: {F}, F crítico: {f_critico}")
        if F > f_critico:
            print("Rechazamos la hipótesis nula H0")
            return
        print("No rechazamos la hipótesis nula H0")
        print("Construimos la docima para medias")
        print("Calculamos estadistico combinado")
        estadistico_combinado = ((n1-1)*varianzaSample1+(n2-1)*varianzaSample2)/(n1+n2-2)

        print(f"Estadístico combinado: {estadistico_combinado}")

        print("Construimos la variable pivotal t")

        t = (mediaSample1 - mediaSample2) / np.sqrt(estadistico_combinado) * np.sqrt(1/n1 + 1/n2)

        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        gl = n1 + n2 - 2
        print(f"T calculado: {t:.2f}")
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
            if abs(t) < t_critico:
                print("Rechazamos la hipótesis nula H0")
            else:
                print("No rechazamos la hipótesis nula H0")
    
    def docima_varianza_desconocidas_diferentes(self, mediaSample1, mediaSample2, varianzaSample1, varianzaSample2, n1, n2):
        alternativa = input("Ingrese la alternativa (mayor, menor, diferente): ").lower()
        alfa = float(input("Ingrese el nivel de significancia (alfa): "))

        # calculamos el t
        t = (mediaSample1 - mediaSample2) / np.sqrt(varianzaSample1/n1 + varianzaSample2/n2)

        gl = (varianzaSample1/n1 + varianzaSample2/n2)**2 / ((varianzaSample1/n1)**2/(n1-1) + (varianzaSample2/n2)**2/(n2-1))
        gl = int(gl)  # Convertir a entero para grados de libertad
        print(f"T calculado: {t:.2f}, Grados de libertad: {gl}")
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
