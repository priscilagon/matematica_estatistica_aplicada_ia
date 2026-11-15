import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
CSV = "rio_negro_cotas.csv"
if not os.path.exists(CSV):  # executando a partir da pasta da aula, dentro do repositório
    CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dados", "rio_negro_cotas.csv")

df = pd.read_csv(CSV, parse_dates=["data"])

# Aula 17 — Vetores e matrizes: a "tabela numérica" que o modelo enxerga
d = df[df["temperatura_c"] < 35]
X = d[["cota_metros", "chuva_mm", "temperatura_c"]].to_numpy()   # matriz de dados
print("Forma da matriz X:", X.shape, "-> (observações, features)")
print("Primeiras 3 linhas:\n", X[:3])

v = X[0]                                  # um vetor: o primeiro dia
print("\nVetor do dia 1:", v, "| dimensão:", v.shape[0])

print("\nVetor de médias das colunas:", X.mean(axis=0).round(3))
print("Matriz transposta X.T:", X.T.shape)

# Operações básicas
A = np.array([[1, 2], [3, 4]]); B = np.array([[5, 6], [7, 8]])
print("\nA + B =\n", A + B)
print("2 * A =\n", 2 * A)
print("A @ B (produto matricial) =\n", A @ B)

# Matriz de médias mensais (12 meses x 3 variáveis)
mensal = d.groupby(d["data"].dt.month)[["cota_metros", "chuva_mm", "temperatura_c"]].mean().round(2)
print("\nMédias mensais (matriz 12x3):\n", mensal)
