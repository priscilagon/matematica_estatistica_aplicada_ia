import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 11 — Probabilidade condicional
A = df["alerta"] == "alto"
B = df["chuva_mm"] > 0

# P(A|B) = P(A e B) / P(B)
p_A_dado_B = (A & B).mean() / B.mean()
print("P(alto | choveu)       = %.4f" % p_A_dado_B)

# P(B|A): NÃO é o mesmo número!
p_B_dado_A = (A & B).mean() / A.mean()
print("P(choveu | alto)       = %.4f" % p_B_dado_A)

# Tabela cruzada de contagens e proporções
tab = pd.crosstab(df["alerta"], B.map({True: "choveu", False: "não choveu"}))
print("\nContagens:")
print(tab)
print("\nProporção de cada alerta DENTRO de cada coluna (condicional a chuva):")
print(pd.crosstab(df["alerta"], B, normalize="columns").round(3))

# Condicional por período: chance de chover em cada período
print("\nP(choveu | período):")
print(B.groupby(df["periodo"]).mean().round(3))
