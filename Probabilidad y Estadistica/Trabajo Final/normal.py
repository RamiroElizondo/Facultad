from scipy.stats import shapiro, kstest, anderson, normaltest, jarque_bera
import pandas as pd
from dependencias import prueba_bondad_ajuste

def test_normalidad(df):
    resultados = []
    
    df = df.loc[:, ~df.columns.duplicated()]
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

def test_normalidad_bondad(df):
    df = df.loc[:, ~df.columns.duplicated()]
    columnas = df.select_dtypes(include=["number"]).columns

    for col in columnas:
        x = df[col].dropna()
        print(f"--------Variable: {col}--------")

        x = df[col].dropna()

        res = prueba_bondad_ajuste(x, bins=8, alpha=0.05)


        print(f"Chi² = {res['chi2']:.3f}  |  gl = {res['df']}  |  χ² crítico = {res['crit']:.3f}")
        #print(f"p-value = {res['p_value']:.4f}")
        print("Decisión:", res["decision"])
