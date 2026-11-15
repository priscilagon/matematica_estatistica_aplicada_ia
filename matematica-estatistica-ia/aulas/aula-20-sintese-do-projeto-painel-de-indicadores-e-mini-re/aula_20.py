import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 20 — Mini-relatório final: um "painel" de indicadores em poucas linhas
from scipy import stats

d = df[(df["temperatura_c"] < 35) & (df["cota_metros"].between(10, 33))]   # dados tratados
ordem = ["enchente", "cheia", "vazante", "seca"]

# 1) Tabela de indicadores por período
tab = d.groupby("periodo")["cota_metros"].agg(
    dias="count", media="mean", mediana="median", dp="std", minimo="min", maximo="max"
).reindex(ordem).round(2)
print(tab)

# 2) Correlações e IC da média
print("\nCorrelação cota x temperatura: %.3f" % d["cota_metros"].corr(d["temperatura_c"]))
t = d["temperatura_c"]
ic = stats.t.interval(0.95, df=len(t) - 1, loc=t.mean(), scale=t.std(ddof=1) / np.sqrt(len(t)))
print("Temperatura média: %.2f °C | IC95%% = [%.2f ; %.2f]" % (t.mean(), ic[0], ic[1]))

# 3) Gráfico-síntese
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(d["data"], d["cota_metros"]); ax[0].set_title("Cota diária (m)")
d.boxplot(column="cota_metros", by="periodo", ax=ax[1]); ax[1].set_title("Cota por período")
plt.suptitle(""); plt.tight_layout()
fig.savefig("painel_rio_negro.png", dpi=150); plt.show()
