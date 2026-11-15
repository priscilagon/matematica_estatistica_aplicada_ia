import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 3 — Mini-relatório parcial (AV1): tabela-resumo + gráfico para o relatório
ordem = ["enchente", "cheia", "vazante", "seca"]

resumo = (df.groupby("periodo")["cota_metros"]
            .agg(dias="count", minimo="min", maximo="max")
            .reindex(ordem))
print(resumo)

# gráfico de linha com a cota diária e o rótulo de cada período
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["data"], df["cota_metros"], color="#2a78d6", linewidth=1.5)
ax.set_title("Cota diária do Rio Negro — Porto de Manaus, 2025 (dados didáticos)")
ax.set_ylabel("Cota (m)")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
fig.savefig("grafico_cota.png", dpi=150)   # arquivo para colar no relatório
plt.show()
