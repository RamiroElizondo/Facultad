"""import pandas as pd
from scipy.stats import shapiro

# Cargar el archivo
df = pd.read_csv("water_potability.csv")

# Seleccionar columnas numéricas (sin ID)
numericas = df.select_dtypes(include=["number"]).columns.difference(["ID_Paciente"])

# Resultado por variable
resultados = []

pd.set_option('display.float_format', '{:.10f}'.format)
for col in numericas:
    data = df[col].dropna()
    
    # Shapiro solo permite hasta 5000 datos
    muestra = data.sample(n=5000, random_state=42) if len(data) > 5000 else data

    stat, p = shapiro(muestra)
    normalidad = "Distribución normal" if p >= 0.05 else "No normal"

    resultados.append({
        "Variable": col,
        "Estadístico Shapiro": stat,
        "p-valor": p,
        "Resultado": normalidad
    })

# Mostrar resultados
df_resultados = pd.DataFrame(resultados)
print(df_resultados)"""
from scipy.stats import shapiro, kstest, anderson, normaltest, jarque_bera
import pandas as pd

def test_normalidad(df):
    resultados = []

    columnas = df.select_dtypes(include=["number"]).columns

    for col in columnas:
        x = df[col].dropna()
        fila = {"Variable": col}

        # Test 1: Shapiro-Wilk
        try:
            stat, p = shapiro(x.sample(n=min(5000, len(x)), random_state=42))
            fila["Shapiro"] = True if p > 0.05 else False
        except:
            fila["Shapiro"] = None

        # Test 2: Kolmogorov-Smirnov
        try:
            stat, p = kstest(x, 'norm', args=(x.mean(), x.std()))
            fila["Smirnov"] = True if p > 0.05 else False
        except:
            fila["Smirnov"] = None

        # Test 3: Anderson-Darling
        try:
            result = anderson(x, dist='norm')
            fila["Anderson"] = True if result.statistic < result.critical_values[2] else False  # nivel 5%
        except:
            fila["Anderson"] = None

        # Test 4: D’Agostino y Pearson
        try:
            stat, p = normaltest(x)
            fila["Pearson"] = True if p > 0.05 else False
        except:
            fila["Pearson"] = None

        # Test 5: Jarque-Bera
        try:
            stat, p = jarque_bera(x)
            fila["JarqueBera"] = True if p > 0.05 else False
        except:
            fila["JarqueBera"] = None

        # Conteo de "True" explícito
        tests = [fila.get(test) for test in ["Shapiro", "Smirnov", "Anderson", "Pearson", "JarqueBera"]]
        positivos = sum(1 for t in tests if t is True)
        fila["Distribución Normal"] = "Sí" if positivos >= 2 else "No"

        resultados.append(fila)

    return pd.DataFrame(resultados)


