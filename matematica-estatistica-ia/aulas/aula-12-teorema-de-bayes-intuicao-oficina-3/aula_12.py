import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 12 — Teorema de Bayes (intuição) — Oficina 3
# Exemplo de sistema de alerta de cheia (valores didáticos)
prev    = 0.30     # P(cheia) antes de qualquer evidência (a priori)
sens    = 0.90     # P(alarme | cheia)           (sensibilidade)
falso_p = 0.08     # P(alarme | não cheia)       (falso positivo)

p_alarme = sens * prev + falso_p * (1 - prev)         # lei da probabilidade total
posteriori = sens * prev / p_alarme                   # Bayes
print("P(alarme)         = %.4f" % p_alarme)
print("P(cheia | alarme) = %.4f" % posteriori)

# Mesma ideia com os DADOS do projeto: H = alerta alto, E = chuva forte (> 10 mm)
H = df["alerta"] == "alto"
E = df["chuva_mm"] > 10
p_H, p_E = H.mean(), E.mean()
p_E_dado_H = (E & H).mean() / H.mean()
bayes = p_E_dado_H * p_H / p_E
direto = (H & E).mean() / E.mean()
print("\nP(alto)=%.3f  P(chuva>10)=%.3f  P(chuva>10 | alto)=%.3f" % (p_H, p_E, p_E_dado_H))
print("P(alto | chuva>10) por Bayes : %.4f" % bayes)
print("P(alto | chuva>10) direto    : %.4f  (devem coincidir)" % direto)
