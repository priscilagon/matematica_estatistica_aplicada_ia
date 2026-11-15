import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 7 — Dispersão e covariância
# Para comparar duas variáveis, usamos apenas dias com leitura válida de temperatura
d = df[df["temperatura_c"] < 35]

print("Covariância cota x temperatura:")
print(np.cov(d["cota_metros"], d["temperatura_c"]).round(3))   # matriz 2x2

print("\nCovariância cota x chuva:")
print(np.cov(d["cota_metros"], d["chuva_mm"]).round(3))

# Mesma relação, unidades diferentes -> covariância muda de valor!
cov_m = np.cov(d["cota_metros"], d["temperatura_c"])[0, 1]
cov_cm = np.cov(d["cota_metros"] * 100, d["temperatura_c"])[0, 1]
print("\ncov (cota em m) = %.3f | cov (cota em cm) = %.3f" % (cov_m, cov_cm))

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].scatter(d["cota_metros"], d["temperatura_c"], s=12, alpha=0.6)
ax[0].set(xlabel="Cota (m)", ylabel="Temperatura (°C)", title="Cota x temperatura")
ax[1].scatter(d["cota_metros"], d["chuva_mm"], s=12, alpha=0.6)
ax[1].set(xlabel="Cota (m)", ylabel="Chuva (mm)", title="Cota x chuva")
plt.tight_layout()
plt.show()
