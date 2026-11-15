import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 16 — Intervalo de confiança, hipótese nula e p-valor
from scipy import stats

t = df.loc[df["temperatura_c"] < 35, "temperatura_c"]

# 1) Intervalo de confiança de 95% para a média (distribuição t)
n, m, s = len(t), t.mean(), t.std(ddof=1)
ep = s / np.sqrt(n)
ic = stats.t.interval(0.95, df=n - 1, loc=m, scale=ep)
print("Temperatura: média = %.3f | IC95%% = [%.3f ; %.3f]" % (m, ic[0], ic[1]))

# 2) Teste de hipótese: H0: a temperatura média na CHEIA é igual à da SECA
cheia = df[(df["periodo"] == "cheia")]["temperatura_c"]
seca = df[(df["periodo"] == "seca") & (df["temperatura_c"] < 35)]["temperatura_c"]
res = stats.ttest_ind(cheia, seca, equal_var=False)       # teste t de Welch
print("\nCheia: %.3f °C | Seca: %.3f °C" % (cheia.mean(), seca.mean()))
print("t = %.3f | p-valor = %.3g" % (res.statistic, res.pvalue))
print("Decisão (alfa = 0,05):", "rejeita H0" if res.pvalue < 0.05 else "não rejeita H0")

# 3) Um caso em que NÃO há diferença: dois sorteios do mesmo conjunto
a = t.sample(60, random_state=1)
b = t.sample(60, random_state=2)
res2 = stats.ttest_ind(a, b, equal_var=False)
print("\nDois sorteios do mesmo conjunto: p-valor = %.3f ->" % res2.pvalue,
      "rejeita H0" if res2.pvalue < 0.05 else "não rejeita H0")
