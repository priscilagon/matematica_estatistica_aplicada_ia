import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 2 — Tabelas de frequência e gráficos
# 1) Variável nominal: espécies registradas
freq = df["especie_coleta"].value_counts()
tabela = pd.DataFrame({"freq_abs": freq,
                       "freq_rel_%": (freq / freq.sum() * 100).round(1)})
print(tabela)
print()

# 2) Variável contínua: agrupar em classes
classes = pd.cut(df["cota_metros"], bins=[8, 12, 16, 20, 24, 28, 36])
print(classes.value_counts().sort_index())

# 3) Quatro gráficos, cada um para um tipo de pergunta
fig, ax = plt.subplots(2, 2, figsize=(11, 7))
freq.plot(kind="bar", ax=ax[0, 0], title="Espécies registradas (barras)")
ax[0, 1].plot(df["data"], df["cota_metros"])
ax[0, 1].set_title("Cota ao longo de 2025 (linha)")
ax[1, 0].hist(df["cota_metros"], bins=12, edgecolor="white")
ax[1, 0].set_title("Distribuição da cota (histograma)")
df.boxplot(column="cota_metros", by="periodo", ax=ax[1, 1])
ax[1, 1].set_title("Cota por período (boxplot)")
plt.suptitle("")
plt.tight_layout()
plt.show()
