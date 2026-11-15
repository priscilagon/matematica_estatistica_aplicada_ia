import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 4 — Média, mediana e moda
x = df["cota_metros"]
print("COTA     média: %.2f | mediana: %.2f" % (x.mean(), x.median()))
print("         (moda de variável contínua quase nunca informa: cada valor aparece ~1 vez)")

c = df["chuva_mm"]
print("CHUVA    média: %.2f | mediana: %.2f | moda: %.1f" %
      (c.mean(), c.median(), c.mode()[0]))

# Moda de variáveis qualitativas (aqui a moda é a medida certa)
print("ALERTA   moda:", df["alerta"].mode()[0])
print("ESPÉCIE  moda:", df["especie_coleta"].mode()[0])

# Efeito de um valor atípico numa janela curta (7 dias em torno de 9/ago)
sem = df[(df["data"] >= "2025-08-06") & (df["data"] <= "2025-08-12")]["cota_metros"]
print("\nSemana de 6 a 12/ago:", list(sem))
print("média: %.2f | mediana: %.2f" % (sem.mean(), sem.median()))

# Medidas por período
print()
print(df.groupby("periodo")["cota_metros"].agg(["mean", "median"]).round(2))
