import pandas as pd
import numpy as np
from itertools import combinations
from scipy.stats import pearsonr, chi2_contingency, chi2, ttest_ind,norm
import scipy.stats as stats




def analizar_dependencias(df):
    #df = pd.read_csv("poblacion_1.csv")

    numericas   = df.select_dtypes(include=["number"]).columns.difference(["ID_Paciente"])
    categoricas = df.select_dtypes(exclude=["number"]).columns

    print("Variables Numéricas: ",len(numericas),"-> ", numericas.tolist())
    print("Variables Categóricas: ",len(categoricas),"-> ", categoricas.tolist())

    rows = []

    # 4. Numérica vs Numérica  (Pearson)
    for col1, col2 in combinations(numericas, 2):
        r, p = pearsonr(df[col1].dropna(), df[col2].dropna())
        rows.append({
            "VarA": col1,
            "VarB": col2,
            "TipoA": "num",
            "TipoB": "num",
            "Test": "Pearson",
            "p-valor": p,
            "Resultado": "Dependientes" if p < 0.05 else "Independientes"
        })

    # 5. Categórica vs Categórica  (Chi-cuadrado)
    for col1, col2 in combinations(categoricas, 2):
        tabla = pd.crosstab(df[col1], df[col2])
        _, p, _, _ = chi2_contingency(tabla)
        rows.append({
            "VarA": col1,
            "VarB": col2,
            "TipoA": "cat",
            "TipoB": "cat",
            "Test": "Chi²",
            "p-valor": p,
            "Resultado": "Dependientes" if p < 0.05 else "Independientes"
        })

    # 6. Numérica vs Categórica (T-test o ANOVA)
    for num, cat in [(n, c) for n in numericas for c in categoricas]:
        grupos = [df.loc[df[cat] == g, num].dropna() for g in df[cat].dropna().unique()]
        if len(grupos) == 2:
            _, p = ttest_ind(*grupos)
            prueba = "T-test"
        else:
            p = np.nan        # aquí podrías poner ANOVA si lo implementás
            prueba = "ANOVA"
        dep = "Dependientes" if p < 0.05 else "Independientes"
        rows.append({
            "VarA": num, "VarB": cat,
            "TipoA": "num", "TipoB": "cat",
            "Test": prueba, "p": p, "Resultado": dep
        })
    # ------------------------------------------------------------------
    # 7. DataFrame final
    # ------------------------------------------------------------------
    dependencias = pd.DataFrame(rows)

    # Opcional: mostrar todo sin truncar (quitar si no lo necesitás)
    pd.set_option("display.max_rows", None, "display.max_columns", None,
                "display.width", 0, "display.max_colwidth", None)
    
    print(dependencias)

    # Guardar si querés:
    # dependencias.to_csv("dependencias_simple.csv", index=False)


def prueba_dependencias(df, variable1, variable2):
    print("\n=== Prueba de Independencia ===")
    print(f"Variables: {variable1} y {variable2}")
    

    #Si ambas son numericas, si ambas son categoricas o si son de distinto tipo
    if variable1 in df.select_dtypes(include=["number"]).columns and variable2 in df.select_dtypes(include=["number"]).columns:
        r, p = pearsonr(df[variable1].dropna(), df[variable2].dropna())
        print(f"Coeficiente de correlación de Pearson: {r}, p-valor: {p}")
    elif variable1 in df.select_dtypes(exclude=["number"]).columns and variable2 in df.select_dtypes(exclude=["number"]).columns:
        tabla = pd.crosstab(df[variable1], df[variable2])
        _, p, _, _ = chi2_contingency(tabla)
        print(f"Chi-cuadrado: {p}")
    else:
        print("Discretizamos la variable ")
    

def prueba_independencia(
        df: pd.DataFrame,
        var_num: str,
        bins: list,
        labels: list,
        var_cat: str,
        alpha: float = 0.05
    ):

    
    # 1) Discretizar variable numérica
    df = df.copy()
    df[f"{var_num}_cat"] = pd.cut(df[var_num], bins=bins, labels=labels, right=False)

    # 2) Tabla de contingencia
    tabla = pd.crosstab(df[f"{var_num}_cat"], df[var_cat])
    print("\n----- Tabla de contingencia -----")
    print(tabla)

    # 3) Chi‑cuadrado con SciPy
    chi2_lib, p, dof, esperada = chi2_contingency(tabla)
    print("\n----- Frecuencias esperadas -----")
    print(pd.DataFrame(esperada, index=tabla.index, columns=tabla.columns).round(2))
    print(f"Chi² (SciPy) : {chi2_lib:.2f}")

    # 4) Chi‑cuadrado manual
    chi2_manual = ((tabla.values - esperada) ** 2 / esperada).sum()
    print(f"Chi² (manual): {chi2_manual:.2f}")

    # 5) Valor crítico
    r, c = tabla.shape
    dof = (r - 1) * (c - 1)
    valor_critico = chi2.ppf(1 - alpha, dof)
    print(f"\nValor crítico χ²(1‑α={1-alpha}) con gl={dof}: {valor_critico:.2f}")

    # 6) Conclusión
    if chi2_manual > valor_critico: 
        print("Se rechaza H₀ → Variables DEPENDIENTES")
    else:
        print("No se rechaza H₀ → Variables INDEPENDIENTES")

def prueba_bondad_ajuste(
    x,
    bins=8,
    alpha=0.05,
    pool_expected_lt5=True,
    ddof_params=2,   # parámetros estimados: mu y sigma
    return_tables=True
):
    """
    Prueba de bondad de ajuste Chi-cuadrado para variable continua
    vs. Normal(mu_hat, sigma_hat).

    Parámetros
    ----------
    x : array-like (Series o lista)
        Datos de la variable continua.
    bins : int o array-like
        - Si int: usa intervalos de ancho uniforme entre min y max.
        - Si array-like: se usan como bordes de los intervalos.
    alpha : float
        Nivel de significancia.
    pool_expected_lt5 : bool
        Si True, fusiona clases contiguas hasta que todas las esperadas >= 5.
    ddof_params : int
        Cantidad de parámetros estimados a restar en los grados de libertad.
        Para Normal con mu y sigma estimados, ddof_params = 2.
    return_tables : bool
        Si True, devuelve también las tablas detalladas.

    Retorna
    -------
    results : dict
        {
          'mu': mu_hat,
          'sigma': sigma_hat,
          'chi2': estadístico,
          'df': grados_de_libertad,
          'crit': chi2_crítico,
          'p_value': p_value,
          'decision': 'Rechazo H0' / 'No rechazo H0',
          'tabla_intervalos': DataFrame (opcional),
          'tabla_aportes': DataFrame (opcional)
        }
    """

    x = pd.Series(x).dropna().astype(float)
    n = len(x)
    mu = x.mean()
    sigma = x.std(ddof=1)

    # 1) Construcción de intervalos
    if np.isscalar(bins):
        edges = np.linspace(x.min(), x.max(), int(bins) + 1)
    else:
        edges = np.asarray(bins, dtype=float)
        if not np.all(np.diff(edges) > 0):
            raise ValueError("Los 'bins' deben venir ordenados y sin superponerse.")

    k = len(edges) - 1

    # 2) Frecuencias observadas
    obs, _ = np.histogram(x, bins=edges)

    # 3) Probabilidades esperadas bajo Normal(mu, sigma)
    cdf_vals = norm.cdf((edges - mu) / sigma)  # Φ((x - μ)/σ)
    p_interval = np.diff(cdf_vals)             # prob esperada en cada intervalo
    exp = n * p_interval

    # ---- Pooling (fusionar clases con E < 5) si hace falta ----
    if pool_expected_lt5:
        # Vamos a fusionar de izquierda a derecha
        new_edges = [edges[0]]
        new_obs = []
        new_exp = []
        new_p = []

        acum_obs = 0
        acum_exp = 0.0
        acum_p   = 0.0

        for i in range(k):
            acum_obs += obs[i]
            acum_exp += exp[i]
            acum_p   += p_interval[i]
            # Cuando la esperada acumulada >= 5, cerramos el bloque
            if acum_exp >= 5:
                new_edges.append(edges[i+1])
                new_obs.append(acum_obs)
                new_exp.append(acum_exp)
                new_p.append(acum_p)
                acum_obs = 0
                acum_exp = 0.0
                acum_p   = 0.0

        # Si quedó algo pendiente al final, lo agrega al último bloque
        if acum_exp > 0:
            # unir con el último intervalo creado
            if len(new_obs) == 0:
                # todo quedó en uno solo
                new_edges = [edges[0], edges[-1]]
                new_obs = [acum_obs]
                new_exp = [acum_exp]
                new_p   = [acum_p]
            else:
                new_edges[-1] = edges[-1]
                new_obs[-1] += acum_obs
                new_exp[-1] += acum_exp
                new_p[-1]   += acum_p

        edges = np.array(new_edges)
        obs   = np.array(new_obs)
        exp   = np.array(new_exp)
        p_interval = np.array(new_p)
        k = len(edges) - 1  # nuevo número de clases

    # 4) Estadístico Chi-cuadrado
    chi2_stat = np.sum((obs - exp) ** 2 / exp)

    # 5) Grados de libertad
    df = k - 1 - ddof_params
    if df <= 0:
        raise ValueError(
            f"Los grados de libertad resultaron <= 0 (df={df}). "
            "Usa menos parámetros a estimar, más clases o no fusiones tanto."
        )

    # 6) Valor crítico y p-valor
    chi2_crit = chi2.ppf(1 - alpha, df)
    p_value = 1 - chi2.cdf(chi2_stat, df)

    decision = "Rechazo H0 (no se ajusta a la Normal)" if chi2_stat > chi2_crit else \
               "No rechazo H0 (los datos son consistentes con la Normal)"

    results = {
        "mu": mu,
        "sigma": sigma,
        "chi2": chi2_stat,
        "df": df,
        "crit": chi2_crit,
        "p_value": p_value,
        "decision": decision
    }

    if return_tables:
        # Tabla 1 (intervalos + esperadas)
        z_lower = (edges[:-1] - mu) / sigma
        z_upper = (edges[1:]  - mu) / sigma
        tabla_intervalos = pd.DataFrame({
            "Límite Inferior": edges[:-1],
            "Límite Superior": edges[1:],
            "Z Inferior": z_lower,
            "Z Superior": z_upper,
            "Frecuencia Relativa Esperada": p_interval,
            "Frecuencia Esperada": exp
        })

        # Tabla 2 (observadas vs esperadas y aportes)
        aportes = (obs - exp) ** 2 / exp
        tabla_aportes = pd.DataFrame({
            "Frecuencias Observadas": obs,
            "Frecuencias Esperadas": exp,
            "(Obs i -Esp i)^2/Esp i": aportes
        })

        results["tabla_intervalos"] = tabla_intervalos
        results["tabla_aportes"] = tabla_aportes

    return results

def prueba_homogeneidad(df1, df2, variable, nombre_df1='Grupo1', nombre_df2='Grupo2', alpha=0.05):
    """
    Realiza una prueba de homogeneidad de chi-cuadrado sobre una variable categórica entre dos poblaciones.

    Parámetros:
    - df1, df2: DataFrames de las dos poblaciones.
    - variable: Nombre de la variable categórica a comparar (string).
    - nombre_df1, nombre_df2: Nombres opcionales para etiquetar los grupos.

    Retorna:
    - Tabla de contingencia, estadístico chi2, grados de libertad, valor p.
    """
    # Copias para no modificar los originales
    df1 = df1.copy()
    df2 = df2.copy()

    # Verificar que la variable exista en ambos dataframes
    if variable not in df1.columns or variable not in df2.columns:
        raise ValueError(f"La variable '{variable}' no está presente en ambos DataFrames.")

    # Agregar columna identificadora del grupo
    df1['Grupo'] = nombre_df1
    df2['Grupo'] = nombre_df2

    # Combinar los dataframes
    combinado = pd.concat([df1, df2], ignore_index=True)

    # Eliminar filas con valores faltantes en la variable
    combinado = combinado.dropna(subset=[variable])

    # Crear tabla de contingencia
    tabla = pd.crosstab(combinado['Grupo'], combinado[variable])

    # Aplicar prueba chi-cuadrado
    chi_calculado, p, dof, _ = stats.chi2_contingency(tabla)

    # Imprimir resultados
    print("Tabla de contingencia:")
    print(tabla)
    print("\nResultados:")
    print(f"Chi-cuadrado: {chi_calculado:.4f}")
    print(f"Grados de libertad: {dof}")
    r, c = tabla.shape
    dof = (r - 1) * (c - 1)
    valor_critico = chi2.ppf(1 - alpha, dof)
    print(f"Chi Tabulado: {valor_critico:.4f}")
    print(f"{chi_calculado:.4f}>{valor_critico:.4f} ??")
    if chi_calculado > valor_critico:
        print("Rechazamos la hipótesis nula: las distribuciones son diferentes.")
    else:
        print("No rechazamos la hipótesis nula: las distribuciones son homogéneas.")

    

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\Ramiro\\OneDrive\\Documentos\\GitHub\\Facultad\\Probabilidad y Estadistica\\Trabajo Final\\poblacion_1.csv")
    analizar_dependencias(df)
    #Poblacion 1
        #Blastos_de_Médula_Osea          Enfermedad_Crónica   num   cat   T-test      NaN    Dependientes 0.00186
        #Conteo_de_Globulos_blancos           Mutación_Genética   num   cat   T-test      NaN    Dependientes 0.00794
        #IMC            Estado_de_Fumado   num   cat   T-test      NaN    Dependientes 0.01919
        #Nivel_de_Hemoglobina                      Género   num   cat   T-test      NaN    Dependientes 0.0086
        #Nivel_de_Hemoglobina          Estado_de_Leucemia   num   cat   T-test      NaN    Dependientes 0.04296
    #Poblacion 2
        #Blastos_de_Médula_Osea          Enfermedad_Crónica   num   cat   T-test      NaN    Dependientes 0.03362
        #Conteo_de_Globulos_rojos           Mutación_Genética   num   cat   T-test      NaN    Dependientes 0.02717
        #Conteo_de_Globulos_rojos    Trastornos_Inmunológicos   num   cat   T-test      NaN    Dependientes 0.03307
