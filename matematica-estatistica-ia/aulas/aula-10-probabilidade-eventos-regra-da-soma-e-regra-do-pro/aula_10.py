import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 10 — Probabilidade básica, eventos, regra da soma e do produto
n = len(df)
A = df["alerta"] == "alto"          # evento A: cota em nível alto
B = df["chuva_mm"] > 0              # evento B: choveu no dia

p_A, p_B = A.mean(), B.mean()
p_AeB = (A & B).mean()
print("P(A)   = %.4f   (%d de %d dias)" % (p_A, A.sum(), n))
print("P(B)   = %.4f" % p_B)
print("P(A e B) = %.4f" % p_AeB)

# Regra da soma: P(A ou B) = P(A) + P(B) - P(A e B)
print("\nRegra da soma  : %.4f" % (p_A + p_B - p_AeB))
print("Contagem direta: %.4f" % (A | B).mean())

# Regra do produto SE fossem independentes: P(A e B) = P(A) * P(B)
print("\nP(A)*P(B)      : %.4f  <- compare com P(A e B) = %.4f" % (p_A * p_B, p_AeB))
print("Dias com A e B: esperado se independentes = %.1f | observado = %d" %
      (n * p_A * p_B, (A & B).sum()))

# Evento complementar
print("\nP(não A) = %.4f" % (1 - p_A))
