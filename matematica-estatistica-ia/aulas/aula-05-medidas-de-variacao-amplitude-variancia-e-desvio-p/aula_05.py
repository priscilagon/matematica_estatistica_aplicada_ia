import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 5 — Amplitude, variância e desvio-padrão (populacional x amostral)
def resumo_disp(s):
    return pd.Series({"n": len(s),
                      "amplitude": s.max() - s.min(),
                      "var_pop": s.var(ddof=0),        # divide por n
                      "var_amostral": s.var(ddof=1),   # divide por n-1
                      "dp_pop": s.std(ddof=0),
                      "dp_amostral": s.std(ddof=1)})

ordem = ["enchente", "cheia", "vazante", "seca"]
tab = (df.groupby("periodo")["cota_metros"].apply(resumo_disp)
         .unstack().reindex(ordem).round(3))
tab["n"] = tab["n"].astype(int)
print(tab)

# CUIDADO: o pandas usa ddof=1 por padrão; o NumPy usa ddof=0.
x = df.loc[df["periodo"] == "cheia", "cota_metros"]
print("\npandas  .std()      :", round(x.std(), 4))
print("numpy   np.std(x)   :", round(np.std(x), 4))
print("numpy   ddof=1      :", round(np.std(x, ddof=1), 4))
