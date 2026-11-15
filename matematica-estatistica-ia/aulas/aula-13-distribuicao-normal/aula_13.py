import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 13 — Distribuição Normal
from scipy import stats

t = df.loc[df["temperatura_c"] < 35, "temperatura_c"]     # sem a leitura atípica
mu, sigma = t.mean(), t.std(ddof=1)
print("Temperatura da água: média = %.3f °C | desvio-padrão = %.3f °C" % (mu, sigma))

# Probabilidades pela normal ajustada
print("\nP(T < 28,0) = %.4f" % stats.norm.cdf(28.0, mu, sigma))
print("P(T > 30,0) = %.4f" % (1 - stats.norm.cdf(30.0, mu, sigma)))
print("P(27 < T < 30) = %.4f" % (stats.norm.cdf(30, mu, sigma) - stats.norm.cdf(27, mu, sigma)))

# Regra 68-95-99,7: o que acontece nos DADOS?
for k in (1, 2, 3):
    dentro = ((t > mu - k * sigma) & (t < mu + k * sigma)).mean()
    print("dentro de %d desvio(s): %.1f%% dos dias" % (k, dentro * 100))

# Histograma + curva normal
x = np.linspace(t.min(), t.max(), 200)
plt.hist(t, bins=15, density=True, edgecolor="white", alpha=0.8)
plt.plot(x, stats.norm.pdf(x, mu, sigma), linewidth=2)
plt.xlabel("Temperatura (°C)"); plt.ylabel("Densidade")
plt.title("Temperatura da água e a curva normal ajustada")
plt.show()
