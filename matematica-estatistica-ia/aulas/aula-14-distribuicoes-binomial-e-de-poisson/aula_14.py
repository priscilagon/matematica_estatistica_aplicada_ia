import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 14 — Distribuições Binomial e Poisson
from scipy import stats

# BINOMIAL: em 30 dias, quantos com alerta "alto"?  (n=30, p = proporção de dias altos)
p = (df["alerta"] == "alto").mean()
n = 30
print("p = %.4f | esperado em 30 dias: %.1f | desvio-padrão: %.2f" %
      (p, n * p, np.sqrt(n * p * (1 - p))))
print("P(X = 10)  = %.4f" % stats.binom.pmf(10, n, p))
print("P(X >= 15) = %.4f" % (1 - stats.binom.cdf(14, n, p)))

# POISSON: nº de dias de chuva forte (> 30 mm) em cada mês
forte = (df["chuva_mm"] > 30).groupby(df["data"].dt.month).sum()
print("\nDias de chuva forte por mês:", list(forte))
lam = forte.mean()
print("lambda (média mensal) = %.3f" % lam)
print("P(0 dias)   = %.4f" % stats.poisson.pmf(0, lam))
print("P(>= 3 dias) = %.4f" % (1 - stats.poisson.cdf(2, lam)))

# Comparação: frequência observada x Poisson
for k in range(0, 5):
    print("k=%d  observado=%d meses | esperado=%.2f meses" %
          (k, (forte == k).sum(), 12 * stats.poisson.pmf(k, lam)))
