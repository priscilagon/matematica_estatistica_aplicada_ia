import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 6 — Quartis, outliers (regra do IQR), normalização e padronização
def limites_iqr(s):
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return q1, q3, iqr, q1 - 1.5 * iqr, q3 + 1.5 * iqr

# 1) Temperatura da água: análise do ano todo
t = df["temperatura_c"]
q1, q3, iqr, li, ls = limites_iqr(t)
print("Temperatura  Q1=%.2f Q3=%.2f IQR=%.2f  limites=[%.2f ; %.2f]" % (q1, q3, iqr, li, ls))
print(df.loc[(t < li) | (t > ls), ["data", "temperatura_c"]])

# 2) Cota: o contexto importa — a regra é aplicada DENTRO de cada período
print()
for p, g in df.groupby("periodo"):
    q1, q3, iqr, li, ls = limites_iqr(g["cota_metros"])
    atip = g[(g["cota_metros"] < li) | (g["cota_metros"] > ls)]
    print("%-9s limites=[%.2f ; %.2f]  atípicos: %s" %
          (p, li, ls, list(zip(atip["data"].dt.strftime("%d/%m"), atip["cota_metros"]))))

# 3) Atípico estatístico NÃO é o mesmo que ERRO. Teste do salto diário:
#    um rio não sobe nem desce 2 m de um dia para o outro.
salto = df["cota_metros"].diff().abs()
print("\nSaltos maiores que 2 m entre dias seguidos:")
print(df.loc[salto > 2, ["data", "cota_metros"]])

# 4) Normalização (min-máx) e padronização (z-score) da cota
x = df["cota_metros"]
x_mm = (x - x.min()) / (x.max() - x.min())
z = (x - x.mean()) / x.std(ddof=0)       # mesmo critério do StandardScaler
print("\nmin-máx: mínimo=%.2f máximo=%.2f" % (x_mm.min(), x_mm.max()))
print("z-score: média=%.2f desvio=%.2f" % (round(z.mean(), 6) + 0.0, z.std(ddof=0)))

# 5) O outlier "achata" a escala min-máx: compare com e sem as leituras atípicas
ok = x[(x > 10) & (x < 33)]
print("\nCom atípicos: 20,00 m vira %.3f" % ((20 - x.min()) / (x.max() - x.min())))
print("Sem atípicos: 20,00 m vira %.3f" % ((20 - ok.min()) / (ok.max() - ok.min())))
