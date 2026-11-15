import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 8 — Correlação de Pearson
from scipy import stats

cols = ["cota_metros", "chuva_mm", "temperatura_c"]
d = df[df["temperatura_c"] < 35]

print("Matriz de correlação (dados válidos):")
print(d[cols].corr().round(3))

r, p = stats.pearsonr(d["cota_metros"], d["temperatura_c"])
print("\nPearson cota x temperatura: r = %.3f (r² = %.3f)" % (r, r**2))

# Efeito de UM valor atípico na correlação
r_com = df["cota_metros"].corr(df["temperatura_c"])
r_sem = d["cota_metros"].corr(d["temperatura_c"])
print("r com a leitura de 38,5 °C: %.3f | sem ela: %.3f" % (r_com, r_sem))

# Mapa de calor simples
fig, ax = plt.subplots(figsize=(4.5, 4))
im = ax.imshow(d[cols].corr(), vmin=-1, vmax=1, cmap="RdBu_r")
ax.set_xticks(range(3)); ax.set_xticklabels(["cota", "chuva", "temp"])
ax.set_yticks(range(3)); ax.set_yticklabels(["cota", "chuva", "temp"])
plt.colorbar(im); plt.tight_layout(); plt.show()
