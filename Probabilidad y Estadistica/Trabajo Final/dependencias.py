import pandas as pd
import numpy as np
from itertools import combinations
from scipy.stats import pearsonr, chi2_contingency, chi2, ttest_ind


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
    """for num, cat in [(n, c) for n in numericas for c in categoricas]:
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
        })"""
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
    print("\n📋 Tabla de contingencia:")
    print(tabla)

    # 3) Chi‑cuadrado con SciPy
    chi2_lib, p, dof, esperada = chi2_contingency(tabla)
    print("\n📊 Frecuencias esperadas:")
    print(pd.DataFrame(esperada, index=tabla.index, columns=tabla.columns).round(2))
    print(f"Chi² (SciPy) : {chi2_lib:.4f}")

    # 4) Chi‑cuadrado manual
    chi2_manual = ((tabla.values - esperada) ** 2 / esperada).sum()
    print(f"Chi² (manual): {chi2_manual:.4f}")

    # 5) Valor crítico
    r, c = tabla.shape
    dof = (r - 1) * (c - 1)
    valor_critico = chi2.ppf(1 - alpha, dof)
    print(f"\nValor crítico χ²(1‑α={1-alpha}) con gl={dof}: {valor_critico:.4f}")

    # 6) Conclusión
    if chi2_manual > valor_critico: 
        print("Se rechaza H₀ → Variables DEPENDIENTES")
    else:
        print("No se rechaza H₀ → Variables INDEPENDIENTES")
    
if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\Ramiro\\OneDrive\\Documentos\\GitHub\\Facultad\\Probabilidad y Estadistica\\Trabajo Final\\poblacion_1.csv")
    analizar_dependencias(df)
    #Conteo_de_Globulos_rojos            Estado_de_Fumado   num   cat   T-test       NaN    Dependiente
    # Nivel_de_Hemoglobina                Urbano_Rural   num   cat   T-test       NaN    Dependientes