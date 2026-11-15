import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 15 — População, amostra e viés de amostragem
rng = np.random.default_rng(15)            # semente fixa = resultados reproduzíveis
pop = df.loc[df["temperatura_c"] < 35, "temperatura_c"]
print("POPULAÇÃO (365 dias): média = %.3f | desvio-padrão = %.3f" % (pop.mean(), pop.std(ddof=0)))

# 1) Amostra aleatória simples, 5 vezes, n = 30
print("\nCinco amostras aleatórias de 30 dias:")
for i in range(5):
    am = pop.sample(30, random_state=int(rng.integers(0, 10**6)))
    print("  amostra %d: média = %.3f" % (i + 1, am.mean()))

# 2) Mil amostras: como as médias variam?
medias = [pop.sample(30, random_state=k).mean() for k in range(1000)]
print("\n1000 amostras: média das médias = %.3f | desvio das médias = %.3f" %
      (np.mean(medias), np.std(medias, ddof=1)))
print("Erro-padrão teórico  sigma/raiz(n) = %.3f" % (pop.std(ddof=0) / np.sqrt(30)))

# 3) Amostra VICIADA: só dias de seca (outubro e novembro)
seca = df[(df["periodo"] == "seca") & (df["temperatura_c"] < 35)]["temperatura_c"]
print("\nViés: média só da seca = %.3f (população: %.3f)" % (seca.mean(), pop.mean()))

plt.hist(medias, bins=25, edgecolor="white")
plt.axvline(pop.mean(), color="black", linestyle="--")
plt.title("1000 médias de amostras (n = 30)")
plt.show()
